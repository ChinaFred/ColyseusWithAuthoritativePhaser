# coding: utf-8
from flask import render_template
import face.server as server


app = server.current.app


@app.route("/simple")
def index_simple():
    server.current.page_title = "Simple"
    return render_template("public/index_simple.html")


@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index():
    server.current.page_title = "Dashboard"
    return render_template("public/index.html", config=server.current)


@app.route("/logs")
def console():
    server.current.page_title = "Logs"
    return render_template("public/view_logs/logs.html", config=server.current)


@app.route("/server_display_state")
def display_state():
    server.current.page_title = "logs > display state"
    server.current.display_state()
    return render_template("public/view_logs/logs.html", config=server.current)


@app.route("/about")
def about():
    server.current.page_title = "About"
    return "All about terminator"


#@app.route("/video_feed")
#def video_feed():
#    return Response(camera.gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


server.current.info("-------------------------------Views initialized------------------------------------")
