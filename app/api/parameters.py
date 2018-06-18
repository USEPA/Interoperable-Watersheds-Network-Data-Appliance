from flask_restplus import Namespace, Resource, fields
from app.models.services import parameter_service as service

api = Namespace('parameters', 'modify parameters')
parameter_model = api.model('Parameter', {
    'parameter_id': fields.Integer,
    'parameter_name' : fields.String
})


@api.route('/')
class ParameterCollection(Resource):

    @api.doc('list_paramters')
    @api.marshal_list_with(parameter_model)
    def get(self):
        """Returns a list of paramters"""
        return service.objects

    @api.doc('create_Parameter')
    @api.expect(parameter_model)
    @api.marshal_with(parameter_model)
    def post(self):
        """Creates a Parameter"""
        return service.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Parameter Not Found')
@api.param('id', 'The Parameter Identifier')
class Parameter(Resource):

    @api.doc('get_Parameter')
    @api.marshal_with(parameter_model)
    def get(self, id):
        """ Fetch a Parameter resource given its id"""
        return service.get(id)

    @api.doc('edit_Parameter')
    @api.expect(parameter_model)
    @api.marshal_with(parameter_model)
    def put(self, id):
        """Update a paramters data given its id"""
        return service.update(id, api.payload)

    @api.doc('delete_Parameter')
    def delete(self, id):
        """Deletes a Parameter given its id"""
        service.delete(id)
        return {}, 204

