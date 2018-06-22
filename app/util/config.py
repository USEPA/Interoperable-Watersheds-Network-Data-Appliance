import os
import logging
from logging.config import dictConfig

basedir = os.path.abspath(os.path.dirname(__file__))
logdir = basedir+'/../logs'


class AppConfig(object):
    SECRET_KEY = 'add random secret key here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(AppConfig):
    Debug = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgres://sos:sensors@localhost:5432/ingest'
    MAX_LOG_BYTES = 1024 * 1024
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(logdir, 'flask.log'),
                'formatter': 'default',
                'maxBytes' : MAX_LOG_BYTES,
            },
        },
        'loggers': {
            'sqlalchemy' : {
                'handlers' : ['file'],
                'level' : 'DEBUG',
                'propagate' : True,
            }
        },
        'root' : {
            'level' : 'INFO',
            'handlers' : ['console']
        }
    })



class TestConfig(AppConfig):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProdConfig(AppConfig):
    Debug = False
    SQLALCHEMY_DATABASE_URI = 'postgres://sos:sensors@database:5432/ingest'
    SQLALCHEMY_ECHO = False
    MAX_LOG_BYTES = 1024 * 1024
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(logdir, 'flask.log'),
                'formatter': 'default',
                'maxBytes' : MAX_LOG_BYTES,
            },
        },
        'loggers': {
            'sqlalchemy' : {
                'handlers' : ['file'],
                'level' : 'INFO',
                'propagate' : True,
            }
        },
        'root' : {
            'level' : 'INFO',
            'handlers' : ['console']
        }
    })


config_by_name = dict(
    development=DevConfig,
    test=TestConfig,
    production=ProdConfig
)
