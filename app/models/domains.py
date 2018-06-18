from . import db

class Parameters(db.Model):
    parameter_id = db.Column(db.Integer, primary_key=True)
    parameter_name = db.Column(db.String, nullable=False, unique=True)

class QualityCheckActions(db.Model):
    quality_check_action_id = db.Column(db.Integer, primary_key=True)
    quality_check_action_name = db.Column(db.String, nullable=False, unique=True)

class QualityCheckOperands(db.Model):
    quality_check_operand_id = db.Column(db.Integer, primary_key=True)
    quality_check_operand_name = db.Column(db.String, nullable=False, unique=True)

class DataQualifiers(db.Model):
    data_qualifier_id = db.Column(db.Integer, primary_key=True)
    data_qualifier_name = db.Column(db.String, nullable=False, unique=True)

class Units(db.Model):
    unit_id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String, nullable=False, unique=True)