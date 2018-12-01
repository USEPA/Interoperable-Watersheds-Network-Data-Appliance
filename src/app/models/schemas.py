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
        # load_only = ('parameter_name','quality_check_operand_name','quality_check_action_name')

    organization_id = field_for(organizations.Organizations, 'organization_id', dump_only=False)
    parameter_id = field_for(domains.Parameters, 'parameter_id', dump_only=False)
    quality_check_operand_id = field_for(domains.QualityCheckOperands, 'quality_check_operand_id', dump_only=False)
    quality_check_action_id = field_for(domains.QualityCheckActions, 'quality_check_action_id', dump_only=False)

    parameter_name = fields.Nested(ParameterSchema, only=('parameter_name'))
    quality_check_operand_name = fields.Nested(QualityCheckOperandSchema, only=('quality_check_operand_name'))
    quality_check_action_name = fields.Nested(QualityCheckActionSchema, only=('quality_check_action_name'))

class OrgParamQualCheckListSchema(ma.ModelSchema):
    class Meta:
        model = organizations.OrganizationParameterQualityChecks
        sqla_session = session
    
    organization_id = field_for(organizations.Organizations, 'organization_id', dump_only=False)
    parameter_name = fields.Nested(ParameterSchema, only=('parameter_name'))
    quality_check_operand_name = fields.Nested(QualityCheckOperandSchema, only=('quality_check_operand_name'))
    quality_check_action_name = fields.Nested(QualityCheckActionSchema, only=('quality_check_action_name'))

class OrganizationSchema(ma.ModelSchema):
    class Meta:
        model = organizations.Organizations
        sqla_session = session

    quality_checks = fields.Nested(OrganizationParameterQualityCheckSchema,many=True)
    
class SensorParameterSchema(ma.ModelSchema):
    class Meta:
        model = sensors.SensorParameters
        sqla_session = session
        # load_only=('parameter_name','unit_name')

    sensor_parameter_id = field_for(sensors.SensorParameters, 'sensor_parameter_id', dump_only=False)
    sensor_id = field_for(sensors.Sensors,'sensor_id', dump_only=False)
    parameter_id = field_for(domains.Parameters, 'parameter_id', dump_only=False)
    unit_id = field_for(domains.Units, 'unit_id', dump_only=False)
    parameter_name = fields.Nested(ParameterSchema, only=('parameter_name'))
    unit_name = fields.Nested(UnitSchema, only=('unit_name'))

class SensorListSchema(ma.ModelSchema):
    class Meta:
        model = sensors.Sensors
        sqla_session = session
        fields = ('sensor_id', 'short_name','org_sensor_id', 'ingest_frequency', 'last_ingest','qc_rules_apply', 'ingest_status')

class SensorSchema(ma.ModelSchema):
    class Meta:
        model = sensors.Sensors
        sqla_session = session

    ingest_frequency = fields.Number(validate=lambda n: 1 <= n <= 60)
    organization_id = field_for(organizations.Organizations,'organization_id', dump_only=False)
    data_qualifier_id = field_for(domains.DataQualifiers,'data_qualifier_id', dump_only=False)
    medium_type_id = field_for(domains.MediumTypes, 'medium_type_id', dump_only=False)
    parameters = fields.Nested(SensorParameterSchema, many=True)

