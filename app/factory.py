import os
from flask import Flask
from flask_cors import CORS
from api import api
from models import db
from config import config_by_name


config_name = os.getenv('FLASK_ENV', default='development')

def bootstrap_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    db.init_app(app)
    api.init_app(app)
    return app



