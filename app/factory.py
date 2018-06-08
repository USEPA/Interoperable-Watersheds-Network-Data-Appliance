from flask import Flask
from flask_cors import CORS
from app.api import api
import json
from app.models import db, sensors
from app.config import config_by_name, basedir


def bootstrap_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv('FLASK_ENV', default='development')])
    CORS(app)
    db.init_app(app)
    api.init_app(app)
    return app


def bootstrap_test_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name['test'])
    db.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
        load_test_data(db)

    return app

def load_test_data(db):
    with open(basedir+'/test/data/init.json') as test_data:
        test_json = test_data.read()
        data = json.loads(test_json)
        sensor = sensors.Sensors(**data)
        db.session.add(sensor)
        db.session.commit()


def deconstruct_test_app(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
