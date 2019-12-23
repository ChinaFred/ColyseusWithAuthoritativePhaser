from server import log
import threading
import face.server as server

c = None


def start_webserver(controler):
    controler.face.start()


class Controler:
    def __init__(self, botname):
        global c
        log("-------------------------------------------------------------------------------------")
        log("-------------------------creating application controler------------------------------")
        # create thread for webserver
        c = self
        self.face = server.Server(botname, c)
        self.faceThread = threading.Thread(name="Face", daemon=True, target=start_webserver, args=[self])
        log("-------------------------PPPPPPPPPPPPPPPPPPPPPPPPP-----------------------------------")
        log(threading.active_count())
        log(threading.enumerate())
        log("-------------------------starting webserver thread-----------------------------------")
        self.faceThread.start()
        log(threading.active_count())
        log(threading.enumerate())

    def get_app(self):
        return self.face.app

    def set_app(self, a):
        self.face.app = a


def get_app():
    return c.face.app


def set_app(a):
    c.face.app = a


def display():
    global c
    log("--------------------------------Current controler------------------------------------")
    log("*************************************************************************************")
    log("face : {}".format(c.face))
    log("faceThread : {}".format(c.faceThread))
    log("*************************************************************************************")


def get_server():
    return c.face

