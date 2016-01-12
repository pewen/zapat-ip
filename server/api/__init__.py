from flask import Flask
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
cors = CORS(app, resources={r"/api/plugs/*": {"origins": "*"}})

# Configurations
app.config.from_object('config')

db = SQLAlchemy(app)

import api.views
