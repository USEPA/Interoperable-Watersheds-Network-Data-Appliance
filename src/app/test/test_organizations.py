import unittest
from base import ApiIntegrationTestCase

class OrganizationsAPITest(ApiIntegrationTestCase):

    def test_get_all(self):
        result = self.client.get('/orgs/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    def test_get_one(self):
        result = self.client.get('/orgs/epa')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Not Found')

    def test_post(self):
        result = self.client.post('/orgs/', json={
            "organization_id": "string",
            "parent_organization_id": "string",
            "name": "string",
            "url": "string",
            "contact_name": "string",
            "contact_email": "string",
            "sos_url": "string",
            "quality_checks" : [
                {
                    "organization_id" : "string",
                    "parameter_id": 79950,
                    "quality_check_operand_id": 3,
                    "quality_check_action_id": 1,
                    "threshold": 0.1149228928
                }]
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')
        result = self.client.get('orgs/string')
        self.assertEqual(result.status_code,200, msg='Expected 200 OK')
    
    def test_delete_one(self):
        result = self.client.delete('/orgs/epar10')
        self.assertEqual(result.status_code, 204, msg="Expected 204 Deleted")
        result = self.client.get('/orgs/epar10')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')
        result = self.client.delete('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')

    def test_put_one(self):
        result = self.client.put('/orgs/epa',json={
            "organization_id" : "epa",
            "sos_url": 'wwww.biscuit.com'
        })
        self.assertEqual(result.status_code, 202, msg="Expected 202 Entity Successfully updated")
        result = self.client.get('/orgs/epa')
        self.assertEqual(result.json['sos_url'], 'wwww.biscuit.com', msg="Expected updated sos_url value to be wwww.biscuit.com")
        result = self.client.put('/orgs/doesntexist')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Organization Not Found')
