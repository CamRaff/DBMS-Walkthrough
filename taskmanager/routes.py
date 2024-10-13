'''
    This file contains the routes for the application
'''

from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    '''
        This function renders the base.html template
    '''
    return render_template("base.html")
