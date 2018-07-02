from flask_restplus import Model, fields
qualifier_model = Model('Data Qualifier', {
    'data_qualifier_id': fields.Integer,
    'data_qualifier_name': fields.String
})

action_model = Model('Quality Check Actions', {
    'quality_check_action_id' : fields.Integer,
    'quality_check_action_name' : fields.String
})

operand_model = Model('Quality Check Operands', {
    'quality_check_operand_id' : fields.Integer,
    'quality_check_operand_name' : fields.String
})

unit_model = Model('Units', {
    'unit_id' : fields.Integer,
    'unit_name' : fields.String
})

medium_model = Model('Medium Type', {
    'medium_type_id' : fields.Integer,
    'medium_type_name' : fields.String
})

parameter_model = Model('Parameter',{
    'parameter_id' : fields.Integer,
    'parameter_name' : fields.String
})

domain_model = Model('domains',{
    'qualifiers' : fields.Nested(qualifier_model, as_list=True),
    'actions' : fields.Nested(action_model, as_list=True),
    'operands' : fields.Nested(operand_model, as_list=True),
    'medium_types' : fields.Nested(medium_model, as_list=True),
    'units' : fields.Nested(unit_model, as_list=True)
})