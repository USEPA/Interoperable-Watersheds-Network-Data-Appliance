from flask_restplus import Api
from flask import jsonify
from werkzeug.exceptions import HTTPException
from .sensors import api as sensors
from .parameters import api as parameters
from .domains import api as domains
from .orgs import api as orgs
from .units import api as units
api = Api(version='0.1', title='Sensor Ingest API',default='sensors', description='A Restful API for scheduling ingests of remote data sensors')
api.add_namespace(sensors)
api.add_namespace(parameters)
api.add_namespace(orgs)
api.add_namespace(domains)
api.add_namespace(units)


@api.errorhandler(Exception)
def handle_error(e):
    return {'message': str(e.orig.args)}, 500