import controllers
import serializers
from flask import Flask
from flask_restplus import Api
from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app



def create_namespaces(api):
    greeter = api.namespace('hello', 'Greets Caller')
    # sensors = api.namespace('sensors', 'Modify Sensors')
    # orgs = api.namespace('organizations', 'Modify Organizations')
    greeter.add_resource(controllers.GreeterController, '/')
    return api

def create_api(app):
    return create_namespaces(Api(app))


