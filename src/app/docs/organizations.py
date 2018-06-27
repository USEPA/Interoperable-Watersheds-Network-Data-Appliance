from flask_restplus import Model, fields
quality_check_model = Model('Organization Parameter Quality Checks',{
    'org_parameter_quality_check_id' : fields.Integer(readonly=True),
    'organization_id' : fields.String,
    'parameter_id' : fields.Integer,
    'quality_check_operand_id' : fields.Integer,
    'quality_check_action_id' : fields.Integer,
    'threshold' : fields.Float
})

organization_model = Model('Organization',{
    'organization_id': fields.String,
    'parent_organization_id' : fields.String,
    'name' : fields.String,
    'url' : fields.String,
    'contact_name' : fields.String,
    'contact_email': fields.String,
    'sos_url' : fields.String,
    'quality_checks' : fields.Nested(quality_check_model, as_list=True)
})