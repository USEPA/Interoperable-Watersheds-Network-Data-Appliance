import unittest
import os
from utils import factory



class ApiIntegrationTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = factory.bootstrap_test_app()
        self.client = self.app.test_client()
        
    
    def tearDown(self):
        factory.deconstruct_test_app(self.app)
        self.app = None
        self.client = None
    