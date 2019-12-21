import tools.general as general
import threading
import face.server as server

c = None


def start_webserver(controler):
    controler.face.start()


class Controler:
    def __init__(self, botname):
        global c
        general.log("-------------------------------------------------------------------------------------")
        general.log("-------------------------creating application controler------------------------------")
        # create thread for webserver
        c = self
        self.face = server.Server(botname, c)
        self.faceThread = threading.Thread(name="Face", daemon=True, target=start_webserver, args=[self])
        general.log("-------------------------PPPPPPPPPPPPPPPPPPPPPPPPP-----------------------------------")
        general.log(threading.active_count())
        general.log(threading.enumerate())
        general.log("-------------------------starting webserver thread-----------------------------------")
        self.faceThread.start()
        general.log(threading.active_count())
        general.log(threading.enumerate())

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
    general.log("--------------------------------Current controler------------------------------------")
    general.log("*************************************************************************************")
    general.log("face : {}".format(c.face))
    general.log("faceThread : {}".format(c.faceThread))
    general.log("*************************************************************************************")


def get_server():
    return c.face

