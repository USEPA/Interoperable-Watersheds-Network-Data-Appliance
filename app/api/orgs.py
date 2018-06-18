from flask_restplus import Namespace, Resource, fields
from app.models.services import organizations_service as service

api = Namespace('orgs', 'modify organizations')

organization_model = api.model('Organization', {
    'organization_id': fields.String,
    'parent_organization_id' : fields.String,
    'name' : fields.String,
    'url' : fields.String,
    'contact_name' : fields.String,
    'contact_email': fields.String,
    'sos_url' : fields.String
})

@api.route('/')
class OrganizationCollection(Resource):
    
    @api.doc('list_sensors')
    @api.marshal_list_with(organization_model)
    def get(self):
        """Returns a list of organizations"""
        return service.objects

    @api.doc('create_sensor')
    @api.expect(organization_model)
    @api.marshal_with(organization_model)
    def post(self):
        """Creates a organization"""
        return service.create(api.payload), 201

@api.route('/<string:id>')
@api.response(404, 'Organization Not Found')
@api.param('id', 'The Organization Identifier')
class Organization(Resource):

    @api.doc('get_organization')
    @api.marshal_with(organization_model)
    def get(self, id):
        """ Fetch a organization resource given its id"""
        return service.get(id)

    @api.doc('edit_organization')
    @api.expect(organization_model)
    @api.marshal_with(organization_model)
    def put(self, id):
        """Update a organiztion data given its id"""
        return service.update(id, api.payload)

    @api.doc('delete_organization')
    def delete(self, id):
        """Deletes a organization given its id"""
        service.delete(id)
        return {}, 204