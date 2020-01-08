from flask import render_template

from app import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/order")
def order():
    return render_template("order.html")
