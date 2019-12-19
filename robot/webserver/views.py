from robot import webserver
from flask import render_template
from robot import config

app = config.current.app


@app.route("/simple")
def index_simple():
    return render_template("public/index_simple.html")


@app.route("/")
def index():
    return render_template("public/index.html", config=config.current)


@app.route("/about")
def about():
    return "All about terminator"



