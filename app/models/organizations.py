from . import db

class Organizations(db.Model):
    organization_id = db.Column(db.String, primary_key=True)
    parent_organization_id = db.Column(db.String)
    name = db.Column(db.String)
    url = db.Column(db.String)
    contact_name = db.Column(db.String)
    contact_email = db.Column(db.String)
    sos_url = db.Column(db.String)
    quality_checks = db.relationship("OrganizationParameterQualityChecks", lazy="joined", cascade="save-update, delete, delete-orphan")

class OrganizationParameterQualityChecks(db.Model):
    org_parameter_quality_check_id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.String, db.ForeignKey('organizations.organization_id'))
    parameter_id = db.Column(db.Integer, db.ForeignKey('parameters.parameter_id'))
    quality_check_operand_id = db.Column(db.Integer, db.ForeignKey('quality_check_operands.quality_check_operand_id'))
    quality_check_action_id = db.Column(db.Integer, db.ForeignKey('quality_check_actions.quality_check_action_id'))
    threshold = db.Column(db.Float)