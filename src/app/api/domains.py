from flask_restplus import Namespace, Resource, fields, Model
from models import services
from docs import domains
qualifier_service = services.data_qualifier_service
actions_service = services.quality_check_action_service
operands_service = services.quality_check_operand_service
medium_service = services.medium_service
units_service = services.units_service

api = Namespace('domains', 'Get domain entities')
api.models[domains.qualifier_model.name] = domains.qualifier_model
api.models[domains.action_model.name] = domains.action_model
api.models[domains.operand_model.name] = domains.operand_model
api.models[domains.medium_model.name] = domains.medium_model
api.models[domains.domain_model.name] = domains.domain_model

@api.route('/')
class Domains(Resource):

    @api.doc('list_domains')
    def get(self):
        domains = dict()
        domains['qualifiers'] = qualifier_service.objects.json
        domains['actions'] = actions_service.objects.json
        domains['operands'] = operands_service.objects.json
        domains['medium_types'] = medium_service.objects.json
        domains['units'] = units_service.objects.json
        return domains