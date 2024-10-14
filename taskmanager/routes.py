'''
    This file contains the routes for the application
'''

from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    '''
        This function renders the base.html template
    '''
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    '''
        This function renders the categories.html template
    '''
    return render_template("categories.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    '''
        This function renders the add_category.html template
    '''
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
