import flask 
from flask_cors import CORS
import json
import os
from api import api
from models import services, db , ma
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
services_dict = {
    'qualifiers' : services.data_qualifier_service,
    'actions' : services.quality_check_action_service,
    'mediums' : services.medium_service,
    'operands' : services.quality_check_operand_service,
    'units' : services.units_service,
    'parameters' : services.parameter_service,
    'organizations': services.organizations_service,
    'sensors' : services.sensors_service
}

def load_model_json( key, data):
    ''' loads an array of dictionaries into the database based on its model class '''
    service = services_dict[key]
    service.create_all(data, use_bulk=True)


def load_test_data(path):
    ''' loads test data into the test sqlite database '''
    with open(config.basedir+'/..'+path) as test_data:
        test_json = test_data.read()
        data = json.loads(test_json)
        for k, v in data.items():
            load_model_json(k,v)


def deconstruct_test_app(app):
    ''' drops all modifications to test database to prepare for the next test '''
    db.init_app(app)
    with app.app_context():
        db.drop_all()
