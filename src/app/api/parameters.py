from flask_restplus import Namespace, Resource, fields, abort
from models import services, session
from docs.domains import parameter_model
from models.schemas import ParameterSchema
from utils.exception import ErrorResponse
from .auth import token_required

detail_schema = ParameterSchema()
list_schema = ParameterSchema(many=True)

service = services.parameter_service

api = Namespace('parameters', 'modify parameters')
api.models[parameter_model.name] = parameter_model


@api.route('/')
class ParameterCollection(Resource):

    @token_required
    @api.doc('list_paramters')
    def get(self):
        """Returns a list of paramters"""
        response = list_schema.dump(service.objects).data
        return response, 200

    @token_required
    @api.doc('create_Parameter')
    @api.expect(parameter_model)
    def post(self):
        """Creates a Parameter"""
        parameter = detail_schema.load(api.payload,session=session)
        if not parameter.errors:
            try:
                parameter = service.create(parameter)
                response = detail_schema.dump(parameter.data).data
                return response, 201
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return { 'errors': parameter.errors }, 422


@api.route('/<int:id>')
@api.response(404, 'Parameter Not Found')
@api.param('id', 'The Parameter Identifier')
class Parameter(Resource):

    @token_required
    @api.doc('get_Parameter')
    def get(self, id):
        """ Fetch a Parameter resource given its id"""
        parameter = service.get(id)
        if not parameter:
            abort(404,'parameter {} Not Found'.format(id))
        response = detail_schema.dump(parameter).data
        return response, 200

    @token_required
    @api.doc('edit_Parameter')
    @api.expect(parameter_model)
    def put(self, id):
        """Update a paramters data given its id"""
        parameter = service.get(id)
        if not parameter:
            abort(404, 'parameter {} Not Found'.format(id))

        parameter = detail_schema.load(api.payload,instance=parameter, partial=True)
        if not parameter.errors:
            try:
                service.update()
                response = detail_schema.dump(parameter.data).data
                return response, 202
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return {'errors': parameter.errors}, 422

    @token_required
    @api.doc('delete_Parameter')
    def delete(self, id):
        """Deletes a Parameter given its id"""
        parameter = service.get(id)
        if not parameter:
            abort(404, 'parameter {} Not Found'.format(id))
        service.delete(parameter)
        return {}, 204
