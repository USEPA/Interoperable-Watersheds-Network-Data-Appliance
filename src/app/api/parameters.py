from flask_restplus import Namespace, Resource, fields
from models import services
from docs.domains import parameter_model
service = services.parameter_service
api = Namespace('parameters', 'modify parameters')
api.models[parameter_model.name] = parameter_model


@api.route('/')
class ParameterCollection(Resource):

    @api.doc('list_paramters')
    def get(self):
        """Returns a list of paramters"""
        return service.objects

    @api.doc('create_Parameter')
    @api.expect(parameter_model)
    def post(self):
        """Creates a Parameter"""
        return service.create(api.payload)


@api.route('/<int:id>')
@api.response(404, 'Parameter Not Found')
@api.param('id', 'The Parameter Identifier')
class Parameter(Resource):

    @api.doc('get_Parameter')
    def get(self, id):
        """ Fetch a Parameter resource given its id"""
        return service.get(id)

    @api.doc('edit_Parameter')
    @api.expect(parameter_model)
    def put(self, id):
        """Update a paramters data given its id"""
        return service.update(id, api.payload)

    @api.doc('delete_Parameter')
    def delete(self, id):
        """Deletes a Parameter given its id"""

        return service.delete(id)

