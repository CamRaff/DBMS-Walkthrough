'''
    This file contains the routes for the application
'''

from flask import render_template, request, redirect, url_for
from taskmanager import app
from taskmanager.models import Category, Task
from taskmanager import db


@app.route("/")
def home():
    '''
        This function renders the base.html template
    '''
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/categories")
def categories():
    '''
        This function renders the categories.html template
    '''
    categories = list(Category.query.order_by(Category.category_name).all()) #noqa
    return render_template("categories.html", categories=categories)

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

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    '''
        This function renders the edit_category.html template
    '''
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    '''
        This function deletes the category
    '''
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    '''
        This function renders the add_category.html template
    '''
    categories = list(Category.query.order_by(Category.category_name).all()) #noqa
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)

@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    '''
        This function renders the add_category.html template
    '''
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all()) #noqa
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    '''
        This function deletes the category
    '''
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))
