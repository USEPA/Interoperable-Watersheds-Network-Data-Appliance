from flask_restplus import Namespace, Resource, fields, abort
from models import services, session
from docs.organizations import quality_check_model, organization_model
from models.schemas import OrganizationSchema
from utils.exception import ErrorResponse

service = services.organizations_service

detail_schema = OrganizationSchema()
list_schema = OrganizationSchema(many=True)

api = Namespace('orgs', 'modify organizations')
api.models[quality_check_model.name] = quality_check_model
api.models[organization_model.name] = organization_model

@api.route('/')
class OrganizationCollection(Resource):
    
    @api.doc('list_orgs')
    def get(self):
        """Returns a list of organizations"""
        response = list_schema.dump(service.objects).data
        return response, 200

    @api.doc('create_org')
    @api.expect(organization_model)
    def post(self):
        """Creates a organization"""
        org = detail_schema.load(api.payload,session=session)
        if not org.errors:
            try:
                org = service.create(org)
                response = detail_schema.dump(org.data).data
                return response, 201
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return { 'errors': org.errors }, 422

@api.route('/<string:id>')
@api.response(404, 'Organization Not Found')
@api.param('id', 'The Organization Identifier')
class Organization(Resource):

    @api.doc('get_organization')
    def get(self, id):
        """ Fetch a organization resource given its id"""
        org = service.get(id)
        if not org:
            abort(404,'org {} Not Found'.format(id))
        response = detail_schema.dump(org).data
        return response, 200

    @api.doc('edit_organization')
    @api.expect(organization_model)
    def put(self, id):
        """Update a organiztion data given its id"""
        org = service.get(id)
        if not org:
            abort(404, 'org {} Not Found'.format(id))

        org = detail_schema.load(api.payload,instance=org, partial=True)
        if not org.errors:
            try:
                service.update()
                response = detail_schema.dump(org.data).data
                return response, 202
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return {'errors': org.errors}, 422

    @api.doc('delete_organization')
    def delete(self, id):
        """Deletes a organization given its id"""
        org = service.get(id)
        if not org:
            abort(404, 'org {} Not Found'.format(id))
        service.delete(org)
        return {}, 204