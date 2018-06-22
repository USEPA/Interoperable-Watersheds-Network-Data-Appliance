from flask_restplus import Namespace, Resource, fields
from models import services
service = services.sensors_service

api = Namespace('sensors', 'modify sensors')

sensor_parameter_model = api.model('Sensor Parameters', {
    'sensor_parameter_id' : fields.Integer(readonly=True),
    'sensor_id' : fields.Integer,
    'parameter_id' : fields.Integer,
    'unit_id' : fields.Integer,
    'parameter_column_id' : fields.Integer
})

sensor_list_model = api.model('Sensor List',{
    'sensor_id' : fields.Integer(readonly=True),
    'short_name' : fields.String,
    'ingest_frequency' : fields.Integer,
    'last_ingest' : fields.DateTime,
    'qc_rules_apply' : fields.Boolean,
    'ingest_status' : fields.String
})

sensor_model = api.model('Sensor', {
    'sensor_id': fields.Integer(readonly=True),
    'organization_id': fields.String,
    'org_sensor_id': fields.String,
    'data_qualifier_id': fields.Integer,
    'medium_type_id' : fields.Integer,
    'short_name': fields.String,
    'long_name': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'altitude': fields.Float,
    'timezone': fields.String,
    'ingest_frequency': fields.Integer,
    'ingest_status': fields.String(readonly=True),
    'last_ingest': fields.DateTime(readonly=True),
    'next_ingest': fields.DateTime(readonly=True),
    'data_url': fields.String,
    'data_format': fields.Integer,
    'timestamp_column_id': fields.Integer,
    'qc_rules_apply': fields.Boolean,
    'active': fields.Boolean,
    'parameters' : fields.Nested(sensor_parameter_model, allow_null=False, as_list=True)
})

@api.route('/')
class SensorCollection(Resource):

    @api.doc('list_sensors')
    @api.marshal_list_with(sensor_list_model)
    def get(self):
        """Returns a list of sensors"""
        return service.objects

    @api.doc('create_sensor')
    @api.expect(sensor_model)
    @api.marshal_with(sensor_model)
    def post(self):
        """Creates a sensor"""
        return service.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Sensor Not Found')
@api.param('id', 'The Sensor Identifier')
class Sensor(Resource):

    @api.doc('get_sensor')
    @api.marshal_with(sensor_model)
    def get(self, id):
        """ Fetch a sensor resource given its id"""
        return service.get(id)

    @api.doc('edit_sensor')
    @api.expect(sensor_model)
    @api.marshal_with(sensor_model)
    def put(self, id):
        """Update a sensors data given its id"""
        
        return service.update(id, api.payload)

    @api.doc('delete_sensor')
    def delete(self, id):
        """Deletes a sensor given its id"""
        service.delete(id)
        return {}, 204
