import unittest
from base import ApiIntegrationTestCase

class DomainsAPITest(ApiIntegrationTestCase):

    def test_get_units(self):
        result = self.client.get('/units/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    def test_get_actions(self):
        result = self.client.get('/actions/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    def test_get_operands(self):
        result = self.client.get('/operands/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
    
    def test_get_qualifiers(self):
        result = self.client.get('/qualifiers/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')