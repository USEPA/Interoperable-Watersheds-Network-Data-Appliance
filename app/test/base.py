import unittest
import os
from app.factory import bootstrap_test_app, deconstruct_test_app


class ApiIntegrationTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = bootstrap_test_app()
        self.client = self.app.test_client()
        
    
    def tearDown(self):
        deconstruct_test_app(self.app)
        self.app = None
        self.client = None
    