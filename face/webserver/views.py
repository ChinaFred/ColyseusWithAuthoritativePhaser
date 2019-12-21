from flask import render_template
import face.server as server
import tools.general as general

app = server.current.app


@app.route("/simple")
def index_simple():
    return render_template("public/index_simple.html")


@app.route("/")
def index():
    general.log("Ouch")
    return render_template("public/index.html", config=server.current)


@app.route("/about")
def about():
    return "All about terminator"


general.log("-------------------------------Views initialized------------------------------------")
