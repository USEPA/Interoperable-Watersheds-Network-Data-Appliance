from . import sensors, domains, organizations, ma, session
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import field_for, fields_for_model

class SensorParameterSchema(ma.ModelSchema):
    class Meta:
        model = sensors.SensorParameters
        sqla_session = session

    sensor_parameter_id = field_for(sensors.SensorParameters, 'sensor_parameter_id', dump_only=False)
    sensor_id = field_for(sensors.Sensors,'sensor_id', dump_only=False)
    parameter_id = field_for(domains.Parameters, 'parameter_id', dump_only=False)
    unit_id = field_for(domains.Units, 'unit_id', dump_only=False)

class SensorSchema(ma.ModelSchema):
    class Meta:
        model = sensors.Sensors
        sqla_session = session

    organization_id = field_for(organizations.Organizations,'organization_id', dump_only=False)
    data_qualifier_id = field_for(domains.DataQualifiers,'data_qualifier_id', dump_only=False)
    medium_type_id = field_for(domains.MediumTypes, 'medium_type_id', dump_only=False)
    parameters = fields.Nested(SensorParameterSchema, many=True)
