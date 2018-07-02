from flask_restplus import Namespace, Resource, fields, abort
from models import services, session
from models.schemas import SensorSchema, SensorListSchema
from ingest.scheduler import add_to_schedule
from docs.sensors import  sensor_parameter_model, sensor_model
from utils.exception import ErrorResponse

service = services.sensors_service

detail_schema = SensorSchema()
list_schema = SensorListSchema(many=True)

api = Namespace('sensors', 'modify sensors')
api.models[sensor_parameter_model.name] = sensor_parameter_model
api.models[sensor_model.name] = sensor_model

@api.route('/')
@api.response(422, 'Invalid Sensor Data')
class SensorCollection(Resource):

    @api.doc('list_sensors')
    def get(self):
        """Returns a list of sensors"""
        response = list_schema.dump(service.objects).data
        return response, 200

    @api.doc('create_sensor')
    @api.expect(sensor_model)
    def post(self):
        """Creates a sensor"""
        sensor = detail_schema.load(api.payload,session=session)
        if not sensor.errors:
            try:
                sensor = service.create(sensor)
                response = detail_schema.dump(sensor.data).data
                return response, 201
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return { 'errors': sensor.errors }, 422


@api.route('/<int:id>')
@api.response(404, 'Sensor Not Found')
@api.response(422, 'Invalid Sensor Data')
@api.param('id', 'The Sensor Identifier')
class Sensor(Resource):

    @api.doc('get_sensor')
    def get(self, id):
        """ Fetch a sensor resource given its id"""
        sensor = service.get(id)
        if not sensor:
            abort(404,'Sensor {} Not Found'.format(id))
        response = detail_schema.dump(sensor).data
        return response, 200

    @api.doc('edit_sensor')
    @api.expect(sensor_model)
    def put(self, id):
        """Update a sensors data given its id"""
        sensor = service.get(id)
        if not sensor:
            abort(404, 'Sensor {} Not Found'.format(id))

        sensor = detail_schema.load(api.payload,instance=sensor, partial=True)
        if not sensor.errors:
            try:
                service.update(data=sensor.data)
                response = detail_schema.dump(sensor.data).data
                return response, 202
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return {'errors': sensor.errors}, 422

    @api.doc('delete_sensor')
    def delete(self, id):
        """Deletes a sensor given its id"""
        sensor = service.get(id)
        if not sensor:
            abort(404, 'Sensor {} Not Found'.format(id))
        try:
            service.delete(sensor)
            return {}, 204
        except Exception as err:
            message = 'There was an error Deleting, Message: '+type(err).__name__+' '+str(err)
            raise ErrorResponse(message,500)