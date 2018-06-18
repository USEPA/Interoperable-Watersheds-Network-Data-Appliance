from flask_restplus import Api
from .sensors import api as sensors

api = Api(version='0.1', title='Sensor Ingest API',default='sensors', description='A Restful API for scheduling ingests of remote data sensors')
api.add_namespace(sensors)