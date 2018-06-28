import unittest
from base import ApiIntegrationTestCase

class DomainsAPITest(ApiIntegrationTestCase):

    def test_get_domains(self):
        result = self.client.get('/domains/')
        self.assertEqual(result.status_code, 200, msg='Expected 200 OK')
        self.assertGreater(len(result.json['qualifiers']),0, msg='Expected qualifier data to be non-empty')
        self.assertGreater(len(result.json['actions']),0, msg='Expected actions data to be non-empty')
        self.assertGreater(len(result.json['operands']),0, msg='Expected operands data to be non-empty')
        self.assertGreater(len(result.json['medium_types']),0, msg='Expected medium types data to be non-empty')