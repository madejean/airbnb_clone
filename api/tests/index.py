from app import ap
from datetime import datetime
import unittest
import json

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_200(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get('/')
        to_json = json.loads(response.data)
        self.assertEqual(to_json['status'],  "OK")

    def test_time(self):
        response = self.app.get('/')
        time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        to_json = json.loads(response.data)
        self.assertEqual(to_json['time'], time)

    def test_time_utc(self):
        utc_time = datetime.uctnow().strftime("%Y/%m/%d %H:%M:%S")
        response = self.app.get('/')
        to_json = json.loads(response.data)
        self.assertEqual(to_json['utc_time'], utc_time)
