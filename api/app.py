from app import app
from config import *

app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
