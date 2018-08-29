import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize application
app = Flask(__name__, static_folder=None)

from crimeapp import dbconfig
# Import the application views
from crimeapp import crimemap

