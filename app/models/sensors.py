from models import db

class Sensors(db.Model):
    __table_name__ = 'sos.sensors'
    
    sensor_id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.String)
    org_sensor_id = db.Column(db.String)
    data_qualifier_id = db.Column(db.Integer)
    short_name = db.Column(db.String)
    long_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    timezone = db.Column(db.String)
    ingest_frequency = db.Column(db.Integer)
    ingest_status = db.Column(db.String(8),default="Unknown")
    last_ingest = db.Column(db.DateTime)
    data_url = db.Column(db.String)
    data_format = db.Column(db.Integer)
    timestamp_column_id = db.Column(db.Integer)
    qc_rules_apply = db.Column(db.Boolean)
    active = db.Column(db.Boolean)

