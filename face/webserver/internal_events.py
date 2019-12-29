from face.server import current as server
from flask import render_template
from flask_socketio import SocketIO


@server.socketio.on('connect')
def test_connect():
    print("connection -----------------------------------------------------------------------------------")
    server.warning("client connected")
    server.socketio.emit('my response', {'data': 'Connected'})


@SocketIO.on('connect')
def test_connect2():
    print("connection -----------------------------------------------------------------------------------")
    server.warning("client connected")
    server.socketio.emit('my response', {'data': 'Connected'})


@SocketIO.on('disconnect')
def test_disconnect():
    server.warning('Client disconnected')


@server.socketio.on('disconnect')
def test_disconnect2():
    server.warning('Client disconnected')


@SocketIO.on('broadcast_notifications')
def broadcast_notifications():
    server.socketio.emit('broadcasted notifications', server.notifications, broadcast=True)


@SocketIO.on('broadcast_console_message')
def broadcast_console_message():
    server.socketio.emit('broadcasted console message', server.notifications, broadcast=True)


@SocketIO.on('new_pds_statuses')
def on_new_pds_statuses():
    print("********************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    server.debug("********************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    server.debug("received broadcasted pds")
    html = render_template("common/templates/cards/proximity_sensors_card/cnt_proximity_sensors_card.html",
                           config=server)
    server.socketio.emit('broadcasted pds statuses', html, broadcast=True)


server.info("---------------------------adding sockets error handling-----------------------------")


@SocketIO.on_error()        # Handles the default namespace
def error_handler(e):
    server.error("error_handler socketio" + str(e))
    pass


@SocketIO.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    server.error("default_error_handler socketio" + str(e))
    pass
