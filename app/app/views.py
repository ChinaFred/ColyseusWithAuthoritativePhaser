from app import app
from flask import render_template


@app.route("/simple")
def index_simple():
    return render_template("public/index_simple.html")


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return "All about terminator"



