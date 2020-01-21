# coding: utf-8
from flask import render_template, Response
import face.server as server
from brain.task import PossibleTasks
from sensors.camera.camera import Camera


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
    return render_template("public/index.html", server=server.current, PossibleTasks=PossibleTasks)


@app.route("/logs")
def console():
    server.current.page_title = "Logs"
    return render_template("public/view_logs/logs.html", server=server.current)


@app.route("/server_display_state")
def display_state():
    server.current.page_title = "logs > display state"
    server.current.display_state()
    return render_template("public/view_logs/logs.html", server=server.current)


@app.route("/about")
def about():
    server.current.page_title = "About"
    return "All about terminator"


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/streaming')
def streaming():
    """Video streaming home page."""
    return render_template('common/templates/cards/camera_card/video_feed_camera_card.html')

server.current.info("-------------------------------Views initialized------------------------------------")
