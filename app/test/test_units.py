import unittest
from base import ApiIntegrationTestCase


class unitsAPITest(ApiIntegrationTestCase):

      
    
    def test_get_all(self):
        result = self.client.get('/units/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    
    def test_post(self):
        result = self.client.post('/units/', json={
            "unit_id": 6,
            "unit_name": "string"
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')
        result = self.client.get('units/6')
        self.assertEqual(result.status_code,200, msg='Expected 200 OK')


    def test_get_one(self):
        result = self.client.get('/units/1')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/units/1239085123')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Unit Not Found')


    def test_delete_one(self):
        result = self.client.delete('/units/1')
        self.assertEqual(result.status_code, 204, msg="Expected 204 Deleted")
        result = self.client.get('/units/1')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Unit Not Found')
        result = self.client.delete('/units/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Unit Not Found')

    
    def test_put_one(self):
        result = self.client.put('/units/1',json={"unit_name": 'biscuit'})
        self.assertEqual(result.status_code, 200, msg="Expected 200 OK")
        result = self.client.get('/units/1')
        self.assertEqual(result.json['unit_name'], 'biscuit', msg="Expected updated unit_name value to be 'biscuit'")
        result = self.client.put('/units/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Unit Not Found')