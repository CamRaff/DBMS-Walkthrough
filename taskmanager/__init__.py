'''
    This file is the entry point to the application. 
    It imports the Flask class from the flask module and creates an instance of this class.
'''

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


db = SQLAlchemy(app)

from taskmanager import routes  # noqa
