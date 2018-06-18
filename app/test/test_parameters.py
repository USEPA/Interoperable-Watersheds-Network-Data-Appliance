import unittest
from base import ApiIntegrationTestCase


class ParametersAPITest(ApiIntegrationTestCase):

      
    
    def test_get_all(self):
        result = self.client.get('/parameters/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    
    def test_post(self):
        result = self.client.post('/parameters/', json={
            "parameter_id": 1,
            "parameter_name": "string"
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')
        result = self.client.get('parameters/1')
        self.assertEqual(result.status_code,200, msg='Expected 200 OK')


    def test_get_one(self):
        result = self.client.get('/parameters/80040')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/parameters/1239085123')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Parameter Not Found')


    def test_delete_one(self):
        result = self.client.delete('/parameters/80040')
        self.assertEqual(result.status_code, 204, msg="Expected 204 Deleted")
        result = self.client.get('/parameters/80040')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Parameter Not Found')
        result = self.client.delete('/parameters/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Parameter Not Found')

    
    def test_put_one(self):
        result = self.client.put('/parameters/80040',json={"parameter_name": 'biscuit'})
        self.assertEqual(result.status_code, 200, msg="Expected 200 OK")
        result = self.client.get('/parameters/80040')
        self.assertEqual(result.json['parameter_name'], 'biscuit', msg="Expected updated parameter_name value to be 'biscuit'")
        result = self.client.put('/parameters/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Parameter Not Found')