import unittest
from base import ApiIntegrationTestCase


class SensorsAPITest(ApiIntegrationTestCase):

    
    def test_get_all(self):
        result = self.client.get('/sensors/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    
    def test_post(self):
        result = self.client.post('/sensors/', json={
            "organization_id": "epar10",
            "org_sensor_id": "string",
            "data_qualifier_id": 1,
            "medium_type_id": 1,
            "short_name": "string",
            "long_name": "string",
            "latitude": 0,
            "longitude": 0,
            "altitude": 0,
            "timezone": "string",
            "ingest_frequency": 15,
            "data_url": "string",
            "data_format": 1,
            "timestamp_column_id": 1,
            "qc_rules_apply": True,
            "active": True,
            "parameters" : [
                {
                    "parameter_id": 79950,
                    "unit_id": 1,
                    "parameter_column_id": 3
                },
                {
                    "parameter_id": 79940,
                    "unit_id": 2,
                    "parameter_column_id": 4
                },
                {
                    "parameter_id": 79960,
                    "unit_id": 3,
                    "parameter_column_id": 5
                },
            ]
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')
        result = self.client.get('sensors/4')
        self.assertEqual(result.status_code,200, msg='Expected 200 OK')


    def test_get_one(self):
        result = self.client.get('/sensors/1')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/sensors/1239085123')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')


    def test_delete_one(self):
        result = self.client.delete('/sensors/1')
        self.assertEqual(result.status_code, 204, msg="Expected 204 Deleted")
        result = self.client.get('/sensors/1')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')
        result = self.client.delete('/sensors/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')

    
    def test_put_one(self):
        result = self.client.put('/sensors/1',json={
            "altitude": 15,
            "parameters" : [{
                "sensor_parameter_id": 1,
                "sensor_id": 1,
                "parameter_id": 79950,
                "unit_id": 1,
                "parameter_column_id": 10
            },
            {
                "sensor_id": 1,
                "parameter_id": 80050,
                "unit_id": 2,
                "parameter_column_id": 5
            }       
        ]})
        self.assertEqual(result.status_code, 200, msg="Expected 200 OK")
        result = self.client.get('/sensors/1')
        self.assertEqual(result.json['altitude'],15, msg="Expected updated altitude value to be 15")
        self.assertEqual(len(result.json['parameters']),2, msg="Expected 2 parameters to exist")
        modified_p = result.json['parameters'][0]
        self.assertEqual(modified_p['parameter_column_id'],10, msg='Expected column id to be 10')
        result = self.client.put('/sensors/123098124')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')