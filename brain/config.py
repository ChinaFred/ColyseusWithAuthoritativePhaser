import os
import tools.general as general
import datetime


current = None



class Config:
    def __init__(self, bot_name):
        self.botName = bot_name
        self.app = None
        self.lastPicture = "/static/img/admin.png"
        self.lastPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.isRunningOnWindows = general.isRunningOnWindows()
        root = ""
        if not self.isRunningOnWindows:
            root = "/terminator"
        self.writePicturePath = os.getcwd() + root + "/face/webserver/static/img/cam/"
        self.hasPiCam = False
        #will be initialized when loading module

    def set_app(self, a):
        self.app = a

    def set_lastPicture(self, filename):
        self.lastPicture = self.readPicturePath+filename
        self.lastPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath+filename))


def init():
    global current
    if current is None:
        print("-------------------------------Initializating bot------------------------------------")
        current = Config("Terminator")
    else:
        print("-------------------------------Already configured------------------------------------")
    return current


def display():
    global current
    print("--------------------------------Current config---------------------------------------")
    print("*************************************************************************************")
    if current is None:
        print("No configuration defined")
    else:
        print("Name : {}".format(current.botName))
        print("app : {}".format(current.app))
        print("lastPicture : {}".format(current.lastPicture))
        print("lastPictureDateTime : {}".format(current.lastPictureDateTime))
        print("readPicturePath : {}".format(current.readPicturePath))
        print("self.writePicturePath : {}".format(current.writePicturePath))
        print("isRunningOnWindows : {}".format(current.isRunningOnWindows))
    print("*************************************************************************************")


def set_app(a):
    global current
    current.set_app(a)


##################################################################


init()