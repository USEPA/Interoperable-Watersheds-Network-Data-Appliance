from flask_restplus import Namespace, Resource, fields
from models import services
from ingest.scheduler import add_to_schedule
from docs.sensors import  sensor_parameter_model, sensor_model

service = services.sensors_service

api = Namespace('sensors', 'modify sensors')
api.models[sensor_parameter_model.name] = sensor_parameter_model
api.models[sensor_model.name] = sensor_model

@api.route('/')
@api.response(422, 'Invalid Sensor Data')
class SensorCollection(Resource):

    @api.doc('list_sensors')
    def get(self):
        """Returns a list of sensors"""
        return service.objects

    @api.doc('create_sensor')
    @api.expect(sensor_model)
    def post(self):
        """Creates a sensor"""
        return service.create(api.payload)


@api.route('/<int:id>')
@api.response(404, 'Sensor Not Found')
@api.response(422, 'Invalid Sensor Data')
@api.param('id', 'The Sensor Identifier')
class Sensor(Resource):

    @api.doc('get_sensor')
    def get(self, id):
        """ Fetch a sensor resource given its id"""
        return service.get(id)

    @api.doc('edit_sensor')
    @api.expect(sensor_model)
    def put(self, id):
        """Update a sensors data given its id"""
        
        return service.update(id, api.payload)

    @api.doc('delete_sensor')
    def delete(self, id):
        """Deletes a sensor given its id"""
        return service.delete(id)
