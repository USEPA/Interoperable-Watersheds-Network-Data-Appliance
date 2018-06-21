import os


basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig(object):
    SECRET_KEY = 'add random secret key here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(AppConfig):
    Debug = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgres://sos:sensors@localhost:5432/ingest'


class TestConfig(AppConfig):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProdConfig(AppConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URI = 'postgres://sos:sensors@database:5432/ingest'
    SQLALCHEMY_ECHO = False


config_by_name = dict(
    development=DevConfig,
    test=TestConfig,
    production=ProdConfig
)
