from flask import Flask
from flask_cors import CORS
from app.api import api
import json
import os
from app.models import db, sensors
from app.config import config_by_name, basedir


# bootstraps Flask app with appropriate extensions
def bootstrap_app():
    ''' bootstraps Flask app with appropriate extensions '''
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv('FLASK_ENV', default='development')])
    CORS(app)
    db.init_app(app)
    api.init_app(app)
    return app


def bootstrap_test_app():
    ''' bootstraps a test application for integration tests '''
    app = Flask(__name__)
    app.config.from_object(config_by_name['test'])
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
        load_test_data(db,'/test/data/init.json')

    return app

# a key value match where a key is matched to a sqlalchemy model object 
# this is used to generically load data from a json file for tests
model_class_dict = {
    'sensors' : sensors.Sensors
}

def load_model_json(db, key, data):
    ''' loads an array of dictionaries into the database based on its model class '''
    models_to_insert = []
    model_class = model_class_dict[key]
    for json in data:
        models_to_insert.append(model_class(**json))
    db.session.bulk_save_objects(models_to_insert)
    db.session.commit()

def load_test_data(db,path):
    ''' loads test data into the test sqlite database '''
    with open(basedir+path) as test_data:
        test_json = test_data.read()
        data = json.loads(test_json)
        for k, v in data.items():
            load_model_json(db,k,v)


def deconstruct_test_app(app):
    ''' drops all modifications to test database to prepare for the next test '''
    db.init_app(app)
    with app.app_context():
        db.drop_all()
