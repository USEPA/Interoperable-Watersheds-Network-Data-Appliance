from flask_restplus import Namespace, Resource, fields, Model
from models import services

qualifier_service = services.data_qualifier_service
actions_service = services.quality_check_action_service
operands_service = services.quality_check_operand_service
medium_service = services.medium_service
units_service = services.units_service

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

api = Namespace('domains', 'Get domain entities')
api.models[qualifier_model.name] = qualifier_model
api.models[action_model.name] = action_model
api.models[operand_model.name] = operand_model
api.models[medium_model.name] = medium_model

domain_model = api.model('Domains', {
    'qualifiers' : fields.Nested(qualifier_model, as_list=True),
    'actions' : fields.Nested(action_model, as_list=True),
    'operands' : fields.Nested(operand_model, as_list=True),
    'medium_types' : fields.Nested(medium_model, as_list=True),
    'units' : fields.Nested(unit_model, as_list=True)
})

@api.route('/')
class Domains(Resource):

    @api.doc('list_domains')
    @api.marshal_with(domain_model)
    def get(self):
        domains = dict()
        domains['qualifiers'] = qualifier_service.objects
        domains['actions'] = actions_service.objects
        domains['operands'] = operands_service.objects
        domains['medium_types'] = medium_service.objects
        domains['units'] = units_service.objects
        return domains