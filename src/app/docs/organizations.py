from flask_restplus import fields
quality_check = {
    'org_parameter_quality_check_id' : fields.Integer(readonly=True),
    'organization_id' : fields.String,
    'parameter_id' : fields.Integer,
    'quality_check_operand_id' : fields.Integer,
    'quality_check_action_id' : fields.Integer,
    'threshold' : fields.Float
}

detail_view = {
    'organization_id': fields.String,
    'parent_organization_id' : fields.String,
    'name' : fields.String,
    'url' : fields.String,
    'contact_name' : fields.String,
    'contact_email': fields.String,
    'sos_url' : fields.String
}