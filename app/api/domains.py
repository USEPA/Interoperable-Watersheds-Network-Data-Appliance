from flask_restplus import Namespace, Resource, fields
from app.models.services import data_qualifier_service as qualifier_service
from app.models.services import quality_check_action_service as actions_service
from app.models.services import quality_check_operand_service as operands_service
from app.models.services import units_service

qualifiers = Namespace('qualifiers', 'Get a list of Data Qualifiers')
qualifier_model = qualifiers.model('Data Qualifier', {
    'data_qualifier_id': fields.Integer,
    'data_qualifier_name' : fields.String
})

actions  = Namespace('actions', 'Get a list of Quality Check Actions')
action_model = actions.model('Quality Check Actions', {
    'quality_check_action_id' : fields.Integer,
    'quality_check_action_name' : fields.String
})

operands = Namespace('operands', 'Get a list of Quality Check Operands')
operand_model = operands.model('Quality Check Operands', {
    'quality_check_operand_id' : fields.Integer,
    'quality_check_operand_name' : fields.String
})

units = Namespace ('units', 'Get a list of units')
unit_model = units.model('Units', {
    'unit_id' : fields.Integer,
    'unit_name' : fields.String
})

@qualifiers.route('/')
class DataQualifierCollection(Resource):

    @qualifiers.doc('list_qualifiers')
    @qualifiers.marshal_list_with(qualifier_model)
    def get(self):
        """Returns a list of data qualifiers"""
        return qualifier_service.objects

@actions.route('/')
class QualityCheckActionCollection(Resource):

    @actions.doc('list_qualifiers')
    @actions.marshal_list_with(action_model)
    def get(self):
        """Returns a list of quality check actions"""
        return actions_service.objects

@operands.route('/')
class QualityCheckOperandCollection(Resource):

    @operands.doc('list_operands')
    @operands.marshal_list_with(operand_model)
    def get(self):
        """Returns a list of quality check operands"""
        return operands_service.objects

@units.route('/')
class UnitCollection(Resource):

    @units.doc('list_units')
    @units.marshal_list_with(unit_model)
    def get(self):
        return units_service.objects