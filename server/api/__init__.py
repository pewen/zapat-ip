from flask import Flask
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password

def init_db():
    with app.app_context():
        db.create_all()
        if not User.query.first():
            user_datastore.create_user(
                email='kevin@example.com',
                password=encrypt_password('password'))
            db.session.commit()

# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)
cors = CORS(app, resources={r"/api/plugs/*": {"origins": "*"}})

# Configurations from config.py
app.config.from_object('config')
# Configuration from instance directory
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from api.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

init_db()

import api.views
