from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from factory import create_app
from util import execute_query
from flask_cors import CORS
import queries

application = create_app('dev')
CORS(application)
api = Api(application)

sensors = api.namespace('sensors','Modify Sensors')

sensor_model = api.model('Sensor',{
    'sensor_id' : fields.Integer(readonly=True),
    'organization_id' : fields.String,
    'org_sensor_id' : fields.String,
    'data_qualifier_id' : fields.Integer,
    'short_name' : fields.String,
    'long_name' : fields.String,
    'latitude' : fields.Float,
    'longitude' : fields.Float,
    'altitude' : fields.Float,
    'timezone' : fields.String,
    'ingest_frequency' : fields.Integer,
    'ingest_status' : fields.String(readonly=True),
    'last_ingest' : fields.DateTime(readonly=True),
    'next_ingest' : fields.DateTime(readonly=True),
    'data_url' : fields.String,
    'data_format' : fields.Integer,
    'timestamp_column_id' : fields.Integer,
    'qc_rules_apply' : fields.Boolean,
    'active' : fields.Boolean
})


@sensors.route('/')
class SensorCollection(Resource):
    @sensors.doc('list_sensors')
    @sensors.marshal_list_with(sensor_model)
    def get(self):
        return execute_query(queries.all_sensors)

    @sensors.doc('create_sensor')
    @sensors.expect(sensor_model)
    def post(self):
        sql = queries.insert_sensor.format(api.payload)
        return execute_query(sql)

if __name__ == '__main__':
    application.run(host='0.0.0.0')