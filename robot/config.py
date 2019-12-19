import os, sys
import datetime

current = None


def isRunningOnWindows():
    if sys.platform.find("linux"):
        ret = True
        print("this is windows")
    else:
        ret = False
        print("this is Linux")
    current.set_isRunningOnWindows(ret)
    return ret


class Config:
    def __init__(self, botName):
        self.botName = botName
        self.app = None
        self.lastPicture = "/static/img/admin.png"
        self.lastPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.isRunningOnWindows = isRunningOnWindows()
        root = ""
        if not self.isRunningOnWindows:
            root = "/Terminator"
        self.writePicturePath = os.getcwd() + root + "/robot/webserver/static/img/cam/"

    def set_app(self, a):
        self.app = a

    def set_lastPicture(self, filename):
        self.lastPicture = self.readPicturePath+filename
        self.lastPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath+filename))

    def set_isRunningOnWindows(self, ret):
        self.isRunningOnWindows = ret




def init():
    global current
    if current is None:
        print("-------------------------------------------------------------------------------------")
        print("-------------------------------Initializating bot------------------------------------")
        current = Config("Terminator")
    else:
        print("-------------------------------------------------------------------------------------")
        print("-------------------------------Already configured------------------------------------")
    return current


def display():
    global current
    print("*************************************************************************************")
    print("--------------------------------Current config---------------------------------------")
    if current is None:
        print("No configuration defined")

    else:
        print("Name : {}".format(current.botName))
        print("app : {}".format(current.app))
    print("*************************************************************************************")


def set_app(a):
    global current
    current.set_app(a)





