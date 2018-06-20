from . import db

class Organizations(db.Model):
    organization_id = db.Column(db.String, primary_key=True)
    parent_organization_id = db.Column(db.String)
    name = db.Column(db.String)
    url = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_email = db.Column(db.String)
    sos_url = db.Column(db.String)