from flask import Flask
from flask_restplus import Api
from factory import create_app, create_api

application = create_app('dev')
api = create_api(application)


if __name__ == '__main__':
    application.run(host='0.0.0.0')