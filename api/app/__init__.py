from flask import Flask
from flask_json import FlaskJSON
from app.views import *

app = Flask(__name__)
json = FlaskJSON(app)
