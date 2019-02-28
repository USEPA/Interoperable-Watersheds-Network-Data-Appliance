from flask_restplus import Namespace, Resource, fields, abort
from models import services , session
from models.schemas import UnitSchema
from docs.domains import unit_model
from utils.exception import ErrorResponse
from .auth import token_required

detail_schema = UnitSchema()
list_schema = UnitSchema(many=True)

service = services.units_service
api = Namespace('units', 'modify units')
api.models[unit_model.name] = unit_model

@api.route('/')
class UnitCollection(Resource):

    @api.doc('list_unit')
    def get(self):
        """Returns a list of unit"""
        response = list_schema.dump(service.objects).data
        return response, 200

    @api.doc('create_unit')
    @api.expect(unit_model)
    def post(self):
        """Creates a unit"""
        unit = detail_schema.load(api.payload,session=session)
        if not unit.errors:
            try:
                unit = service.create(unit)
                response = detail_schema.dump(unit.data).data
                return response, 201
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return { 'errors': unit.errors }, 422


@api.route('/<int:id>')
@api.response(404, 'unit Not Found')
@api.param('id', 'The unit Identifier')
class Unit(Resource):

    @api.doc('get_unit')
    def get(self, id):
        """ Fetch a unit resource given its id"""
        unit = service.get(id)
        if not unit:
            abort(404,'unit {} Not Found'.format(id))
        response = detail_schema.dump(unit).data
        return response, 200

    @api.doc('edit_unit')
    @api.expect(unit_model)
    def put(self, id):
        """Update a paramters data given its id"""
        unit = service.get(id)
        if not unit:
            abort(404, 'unit {} Not Found'.format(id))

        unit = detail_schema.load(api.payload,instance=unit, partial=True)
        if not unit.errors:
            try:
                service.update()
                response = detail_schema.dump(unit.data).data
                return response, 202
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return {'errors': unit.errors}, 422

    @api.doc('delete_unit')
    def delete(self, id):
        """Deletes a unit given its id"""
        sensor = service.get(id)
        if not sensor:
            abort(404, 'Sensor {} Not Found'.format(id))
        service.delete(sensor)
        return {}, 204

