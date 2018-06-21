from flask import Flask
from flask_cors import CORS

import json
import os
from api import api
from models import schemas, db , ma
from . import config


def bootstrap_app():
    ''' bootstraps Flask app with appropriate extensions '''
    app = Flask(__name__)
    app.config.from_object(config.config_by_name[os.getenv('FLASK_ENV', default='development')])
    CORS(app)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    return app


def bootstrap_test_app():
    ''' bootstraps a test application for integration tests '''
    app = Flask(__name__)
    app.config.from_object(config.config_by_name['test'])
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
        load_test_data(db,'/test/data/init.json')

    return app

# a key value match where a key is matched to a sqlalchemy model object 
# this is used to generically load data from a json file for tests
model_schema_dict = {
    'qualifiers' : schemas.DataQualifierSchema(),
    'actions' : schemas.QualityCheckActionSchema(),
    'mediums' : schemas.MediumTypeSchema(),
    'operands' : schemas.QualityCheckOperandSchema(),
    'units' : schemas.UnitSchema(),
    'parameters' : schemas.ParameterSchema(),
    'organizations': schemas.OrganizationSchema(),
    'sensors' : schemas.SensorSchema()
}

def load_model_json(db, key, data):
    ''' loads an array of dictionaries into the database based on its model class '''
    models_to_insert = []
    model_schema = model_schema_dict[key]
    models_to_insert.extend(model_schema.load(data, session=db.session, many=True).data)
    db.session.bulk_save_objects(models_to_insert)#use bulk save here for more speed during tests
    db.session.commit()

def load_test_data(db,path):
    ''' loads test data into the test sqlite database '''
    with open(config.basedir+'/..'+path) as test_data:
        test_json = test_data.read()
        data = json.loads(test_json)
        for k, v in data.items():
            load_model_json(db,k,v)


def deconstruct_test_app(app):
    ''' drops all modifications to test database to prepare for the next test '''
    db.init_app(app)
    with app.app_context():
        db.drop_all()
