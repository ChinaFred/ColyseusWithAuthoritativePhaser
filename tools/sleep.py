from face import server


def sleep(t):
    server.current.socketio.sleep(t)
