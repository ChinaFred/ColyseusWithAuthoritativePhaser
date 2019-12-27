from flask import render_template
import face.server as server
from face.server import log
import sensors.camera as camera


app = server.current.app


@app.route("/simple")
def index_simple():
    return render_template("public/index_simple.html")


@app.route("/index.html")
@app.route("/index")
@app.route("/")
def index():
    return render_template("public/index.html", config=server.current)


@app.route("/logs")
def console():
    return render_template("public/view_logs/logs.html", config=server.current)


@app.route("/server_display_state")
def display_state():
    server.current.display_state()
    return render_template("public/view_logs/logs.html", config=server.current)


@app.route("/about")
def about():
    return "All about terminator"


#@app.route("/video_feed")
#def video_feed():
#    return Response(camera.gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


log("-------------------------------Views initialized------------------------------------")
