import os
import datetime

current = None


class Config:
    def __init__(self, botName):
        self.botName = botName
        self.app = None
        self.lastPicture = "/static/img/admin.png"
        self.lastPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.writePicturePath = os.getcwd() + "/terminator/robot/webserver/static/img/cam/"

    def set_app(self, a):
        self.app = a

    def set_lastPicture(self, filename):
        self.lastPicture = self.readPicturePath+filename
        self.lastPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath+filename))


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





