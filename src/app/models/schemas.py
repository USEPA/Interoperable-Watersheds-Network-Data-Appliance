from . import sensors, domains, organizations, ma, session
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import field_for, fields_for_model


class DataQualifierSchema(ma.ModelSchema):
    class Meta: 
        model = domains.DataQualifiers
        sqla_session = session


class QualityCheckActionSchema(ma.ModelSchema):
    class Meta:
        model = domains.QualityCheckActions
        sqla_session = session


class QualityCheckOperandSchema(ma.ModelSchema):
    class Meta:
        model = domains.QualityCheckOperands
        sqla_session = session


class MediumTypeSchema(ma.ModelSchema):
    class Meta:
        model = domains.MediumTypes
        sqla_session = session


class UnitSchema(ma.ModelSchema):
    class Meta:
        model = domains.Units
        sqla_session = session


class ParameterSchema(ma.ModelSchema):
    class Meta:
        model = domains.Parameters
        sqla_session = session        


class OrganizationParameterQualityCheckSchema(ma.ModelSchema):
    class Meta:
        model = organizations.OrganizationParameterQualityChecks
        sqla_session = session

    organization_id = field_for(organizations.Organizations, 'organization_id', dump_only=False)
    parameter_id = field_for(domains.Parameters, 'parameter_id', dump_only=False)
    quality_check_operand_id = field_for(domains.QualityCheckOperands, 'quality_check_operand_id', dump_only=False)
    quality_check_action_id = field_for(domains.QualityCheckActions, 'quality_check_action_id', dump_only=False)
    

class OrganizationSchema(ma.ModelSchema):
    class Meta:
        model = organizations.Organizations
        sqla_session = session

    quality_checks = fields.Nested(OrganizationParameterQualityCheckSchema,many=True)

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
