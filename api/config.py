import os

basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig(object):
    SCRET_KEY = 'add random secret key here'
    DATABASE_URI = 'path to database'
    DEBUG = False

class DevConfig(AppConfig):
    Debug = True

class ProdConfig(AppConfig):
    Debug = False


config_by_name = dict(
    dev=DevConfig,
    prod=ProdConfig
)