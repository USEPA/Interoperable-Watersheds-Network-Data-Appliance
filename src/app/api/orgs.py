from flask_restplus import Namespace, Resource, fields, abort
from models import services, organizations, session
from docs.organizations import quality_check_model, organization_model
from models.schemas import OrganizationSchema, OrganizationParameterQualityCheckSchema
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

qual_check_service = services.org_qual_checks_service

qual_detail_schema = OrganizationParameterQualityCheckSchema()
qual_list_schema = OrganizationParameterQualityCheckSchema(many=True)


@api.route('/<string:orgId>/qualitychecks')
@api.response(404, 'Organization Not Found')
@api.param('orgId', 'The Organization Identifier')
class ParameterQualityCheckCollection(Resource):
    
    @api.doc('list quality checks by Organization Identifier')
    def get(self, orgId):
        qualchecks = qual_check_service.query().filter_by(organization_id=orgId).all()
        if not qualchecks:
            abort(404,'No Parameter Quality Checks found for Organization {} '.format(orgId))
        response = qual_list_schema.dump(qualchecks).data
        return response, 200
    

    @api.doc('create org quality check')
    @api.expect(quality_check_model)
    def post(self, orgId):
        api.payload['organization_id'] = orgId
        qual_check = qual_detail_schema.load(api.payload, session=session)
        
        if not qual_check.errors:
            try:
                qual_check = qual_check_service.create(qual_check)
                response = qual_detail_schema.dump(qual_check.data).data
                return response, 201
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return { 'errors': qual_check.errors }, 422


@api.route('/<string:orgId>/qualitychecks/<int:id>')
@api.response(404, 'Organization Not Found')
@api.response(404, 'Parameter Quality Check Not Found')
@api.param('orgId', 'Organization Identifier')
@api.param('id', 'Parameter Quality check Identifier')
class ParameterQualityCheck(Resource):
    
    @api.doc('get parameter quality check')
    def get(self, orgId, id):
        qc = qual_check_service.query().filter_by(organization_id=orgId, org_parameter_quality_check_id=id).first()
        if not qc:
            abort(404, 'Parameter Quality Check {} Not Found for Organization {}'.format(id,orgId))
        response = qual_detail_schema.dump(qc).data
        return response, 200
    
    @api.doc('update parameter quailty check')
    @api.expect(quality_check_model)
    def put(self, orgId, id):
        qc = qual_check_service.query().filter_by(organization_id=orgId, org_parameter_quality_check_id=id).first()
        if not qc:
            abort(404, 'Parameter Quality Check {} Not Found for Organization {}'.format(id,orgId))
        
        qc = detail_schema.load(api.payload,instance=qc, partial=True)
        if not qc.errors:
            try:
                qual_check_service.update()
                response = qual_detail_schema.dump(qc.data).data
                return response, 202
            except Exception as err:
                message = 'There was an error saving. Message: '+type(err).__name__+' '+str(err)
                raise ErrorResponse(message,500,api.payload)
        return {'errors': org.errors}, 422

    @api.doc('delete parameter quality check')
    def delete(self, orgId, id):
        qc = qual_check_service.query().filter_by(organization_id=orgId, org_parameter_quality_check_id=id).first()
        if not qc:
            abort(404, 'Parameter Quality Check {} Not Found for Organization {}'.format(id,orgId))
        
        qual_check_service.delete(qc)
        return {}, 204
