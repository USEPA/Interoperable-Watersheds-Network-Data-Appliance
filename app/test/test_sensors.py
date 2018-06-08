import unittest
from app.factory import bootstrap_test_app, deconstruct_test_app


class SensorsAPITest(unittest.TestCase):

    
    def setUp(self):
        self.app = bootstrap_test_app()
        self.client = self.app.test_client()
        
    
    def tearDown(self):
        deconstruct_test_app(self.app)
        self.app = None
        self.client = None
    
    
    def test_get_all(self):
        result = self.client.get('/sensors/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    
    def test_post(self):
        result = self.client.post('/sensors/', json={
            "organization_id": "epar10",
            "org_sensor_id": "string",
            "data_qualifier_id": 1,
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
            "active": True
        })
        self.assertEqual(result.status_code, 201, msg='Expected 201 Created')


    def test_get_one(self):
        result = self.client.get('/sensors/1')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        result = self.client.get('/sensors/1239085123')
        self.assertEqual(result.status_code, 404, msg='Expected 404 Sensor Not Found')

if __name__ == '__main__':
    unittest.main()