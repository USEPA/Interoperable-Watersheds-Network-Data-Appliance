import unittest
from app import application


class SensorsAPITest(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()
    
    def test_get_all(self):
        result = self.app.get('/sensors/')
        self.assertEquals(result.status_code, 200, msg='Expected 200 OK')

if __name__ == '__main__':
    unittest.main()