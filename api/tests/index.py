import os
import flaskr
import unittest

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_200(self):
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        with app.test_client() as client:
            response = client.get('/')
            self.asserTrue(status.