from flask_restplus import fields
from .base import build_generic_view
parameter_view = {
    'sensor_parameter_id' : fields.Integer(readonly=True),
    'sensor_id' : fields.Integer,
    'parameter_id' : fields.Integer,
    'unit_id' : fields.Integer,
    'parameter_column_id' : fields.Integer
}

list_view = {
    'sensor_id' : fields.Integer(readonly=True),
    'short_name' : fields.String,
    'ingest_frequency' : fields.Integer,
    'last_ingest' : fields.DateTime,
    'qc_rules_apply' : fields.Boolean,
    'ingest_status' : fields.String
}

detail_view = {
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
    'parameters' : fields.Nested(parameter_view, allow_null=False, as_list=True)
}