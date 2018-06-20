from . import db


class Sensors(db.Model):
    sensor_id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.ForeignKey("organizations.organization_id"), nullable=False)
    org_sensor_id = db.Column(db.String)
    data_qualifier_id = db.Column(db.ForeignKey('data_qualifiers.data_qualifier_id'), nullable=False)
    medium_type_id = db.Column(db.ForeignKey('medium_types.medium_type_id'), nullable=False)
    short_name = db.Column(db.String)
    long_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    timezone = db.Column(db.String)
    ingest_frequency = db.Column(db.Integer)
    ingest_status = db.Column(db.String(8),default="Unknown")
    last_ingest = db.Column(db.DateTime)
    next_ingest = db.Column(db.DateTime)
    data_url = db.Column(db.String)
    data_format = db.Column(db.Integer)
    timestamp_column_id = db.Column(db.Integer)
    qc_rules_apply = db.Column(db.Boolean)
    active = db.Column(db.Boolean)

class SensorParameters(db.Model):
    sensor_id = db.Column(db.ForeignKey('sensors.sensor_id'), primary_key=True)
    parameter_id = db.Column(db.ForeignKey('parameters.parameter_id'), primary_key=True)
    unit_id = db.Column(db.ForeignKey('units.unit_id'), nullable=False)
    parameter_column_id = db.Column(db.Integer)