from flask import Flask
from flask_cors import CORS
from app.api import api_app
from app.client import client_app

app = Flask(__name__)
CORS(app)

# register blueprints
app.register_blueprint(api_app)
app.register_blueprint(client_app)
