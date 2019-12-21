import tools.general as general
import datetime
import os

current = None


class Server:
    def __init__(self, bot_name):
        global current
        general.log("-------------------------------Initializating webserver-----------------------------")
        self.botName = bot_name
        self.lastPicture = "/static/img/admin.png"
        self.lastPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.isRunningOnWindows = general.isRunningOnWindows()
        root = ""
        if not self.isRunningOnWindows:
            root = "/terminator"
        self.writePicturePath = os.getcwd() + root + "/face/webserver/static/img/cam/"
        self.app = None
        #self.controler = c
        current = self

    def set_last_picture(self, filename):
        self.lastPicture = self.readPicturePath+filename
        self.lastPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath+filename))

    def start(self):
        general.log("----------------------------importing webserver config---------------------------------")
        from face import webserver
        self.display_state()
        general.log("------------------------------starting webserver-------------------------------------")
        self.app.run(debug=True, port=80, host='0.0.0.0')

    def display_state(self):
        general.log("--------------------------------Current server config--------------------------------")
        general.log("*************************************************************************************")
        general.log("Name : {}".format(self.botName))
        general.log("lastPicture : {}".format(self.lastPicture))
        general.log("lastPictureDateTime : {}".format(self.lastPictureDateTime))
        general.log("readPicturePath : {}".format(self.readPicturePath))
        general.log("self.writePicturePath : {}".format(self.writePicturePath))
        general.log("isRunningOnWindows : {}".format(self.isRunningOnWindows))
        general.log("app.root_path: " + self.app.root_path)
        general.log("app.instance_path: " + self.app.instance_path)
        general.log("app: " + str(self.app))
        general.log("*************************************************************************************")
