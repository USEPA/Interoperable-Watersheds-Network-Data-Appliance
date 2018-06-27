from flask_restplus import Namespace, Resource, fields
from models import services
from docs.organizations import quality_check_model, organization_model
service = services.organizations_service
api = Namespace('orgs', 'modify organizations')
api.models[quality_check_model.name] = quality_check_model
api.models[organization_model.name] = organization_model

@api.route('/')
class OrganizationCollection(Resource):
    
    @api.doc('list_sensors')
    def get(self):
        """Returns a list of organizations"""
        return service.objects

    @api.doc('create_sensor')
    @api.expect(organization_model)

    def post(self):
        """Creates a organization"""
        return service.create(api.payload), 201

@api.route('/<string:id>')
@api.response(404, 'Organization Not Found')
@api.param('id', 'The Organization Identifier')
class Organization(Resource):

    @api.doc('get_organization')
    def get(self, id):
        """ Fetch a organization resource given its id"""
        return service.get(id)

    @api.doc('edit_organization')
    @api.expect(organization_model)
    def put(self, id):
        """Update a organiztion data given its id"""
        return service.update(id, api.payload)

    @api.doc('delete_organization')
    def delete(self, id):
        """Deletes a organization given its id"""

        return service.delete(id)