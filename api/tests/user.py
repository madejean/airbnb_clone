from app import app
from app.models.base import db
from datetime import datetime
import unittest
import json

class FlaskrTestCase(unittest.TestCase): 
    def setUp(self):
        self.client = app.test_client()
        logging.disable(logging.CRITICAL)
        db.connect()
        db.create_table('User', safe = True)
        db.close()

        def tearDown(self):
            db.drop_tables('User')
