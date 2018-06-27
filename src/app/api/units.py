from flask_restplus import Namespace, Resource, fields
from models import services
from docs.domains import unit_model
service = services.units_service
api = Namespace('units', 'modify units')
api.models[unit_model.name] = unit_model

@api.route('/')
class UnitCollection(Resource):

    @api.doc('list_unit')
    def get(self):
        """Returns a list of unit"""
        return service.objects

    @api.doc('create_unit')
    @api.expect(unit_model)
    def post(self):
        """Creates a unit"""
        return service.create(api.payload)


@api.route('/<int:id>')
@api.response(404, 'unit Not Found')
@api.param('id', 'The unit Identifier')
class Unit(Resource):

    @api.doc('get_unit')
    def get(self, id):
        """ Fetch a unit resource given its id"""
        return service.get(id)

    @api.doc('edit_unit')
    @api.expect(unit_model)
    def put(self, id):
        """Update a paramters data given its id"""
        return service.update(id, api.payload)

    @api.doc('delete_unit')
    def delete(self, id):
        """Deletes a unit given its id"""

        return service.delete(id)

