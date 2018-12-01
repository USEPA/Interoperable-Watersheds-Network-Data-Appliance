import flask 
from flask_cors import CORS
import json
import os
from api import api
from models import schemas, db , ma
from . import config
from flask_logconfig import LogConfig

def bootstrap_app():
    ''' bootstraps Flask app with appropriate extensions '''
    app = flask.Flask(__name__)
    app.config.from_object(config.config_by_name[os.getenv('FLASK_ENV', default='development')])
    LogConfig(app)
    CORS(app)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    return app


def bootstrap_test_app():
    ''' bootstraps a test application for integration tests '''
    app = flask.Flask(__name__)
    app.config.from_object(config.config_by_name['test'])
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
        load_test_data('/test/data/init.json')

    return app

# a key value match where a key is matched to a sqlalchemy model object 
# this is used to generically load data from a json file for tests
schemas_dict = {
    'qualifiers' : schemas.DataQualifierSchema(many=True),
    'actions' : schemas.QualityCheckActionSchema(many=True),
    'mediums' : schemas.MediumTypeSchema(many=True),
    'operands' : schemas.QualityCheckOperandSchema(many=True),
    'units' : schemas.UnitSchema(many=True),
    'parameters' : schemas.ParameterSchema(many=True),
    'organizations': schemas.OrganizationSchema(many=True),
    'sensors' : schemas.SensorSchema(many=True)
}

def load_model_json(session, key, data):
    ''' loads an array of dictionaries into the database based on its model class '''
    schema = schemas_dict[key]
    collection = schema.load(data,session=session,many=True)
    session.bulk_save_objects(collection.data)
    session.commit()


def load_test_data(path):
    ''' loads test data into the test sqlite database '''
    with open(config.basedir+'/..'+path) as test_data:
        test_json = test_data.read()
        data = json.loads(test_json)
        for k, v in data.items():
            load_model_json(db.session,k,v)


def deconstruct_test_app(app):
    ''' drops all modifications to test database to prepare for the next test '''
    db.init_app(app)
    with app.app_context():
        db.drop_all()
