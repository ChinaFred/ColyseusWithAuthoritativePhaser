import datetime
import flask
from flask import render_template
from face.server import log
import face.server as server
from flask_socketio import emit
from flask_socketio import SocketIO


log("------------------------------creating webserver-------------------------------------")
app = flask.Flask(__name__, static_url_path="/static")
server.current.app = app
socketio = SocketIO(app,  logger=True, engineio_logger=True)
server.current.socketio = socketio


log("------------------------prepare server error messages--------------------------------")


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def ma_page_erreur(error):
    server.error("--------------------------------Error during a call----------------------------------")
    server.error(str(error))
    return render_template("public/errorpage.html", err=error, config=server.current)


log("--------------------------------Loading routes---------------------------------------")
from face.webserver import views
from face.webserver import admin_views
from face.webserver import views_submit
from face.webserver import views_ajax


log("--------------------------Creating template filters----------------------------------")


@app.template_filter()
def datetime_filter(value, f='%d-%m-%Y'):
    ret = ""
    if value:
        """Convert a datetime to a different format."""
        ret = datetime.datetime.strftime(value, f)
    return " " + ret


app.jinja_env.filters['datetime_filter'] = datetime_filter


log("---------------------------adding sockets routes-- ----------------------------------")


@socketio.on('broadcast_notifications')
def broadcast_notifications():
    emit('broadcasted notifications', server.notifications, broadcast=True)


@socketio.on('broadcast_console_message')
def broadcast_console_message():
    emit('broadcasted console message', server.notifications, broadcast=True)


@socketio.on('client connexion')
def client_connect():
    log('client connected')


log("---------------------------adding sockets error handling-----------------------------")


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    server.error("error_handler socketio" + str(e))
    pass


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    server.error("default_error_handler socketio" + str(e))
    pass

