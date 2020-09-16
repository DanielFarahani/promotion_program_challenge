import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(32)

# Enable debug mode.
DEBUG = True

# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'postgres://df@localhost:5432/promodb'
