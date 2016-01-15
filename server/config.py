# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Statement for enabling the development environment
DEBUG = True

# Define the database - we are working with SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
#DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 4

# Enable protection agains *Cross-site Request Forgery (CSRF)*
#CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
#CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
# Get from https://www.grc.com/passwords.htm
SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Set config values for Flask-Security.
# We're using pbkdf2_sha512 with salt.
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
# Replace this with your own salt.
SECURITY_PASSWORD_SALT = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
