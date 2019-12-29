import tools.console_message as cm
from tools.notification import create_info, create_error, create_warning
from tools.toolbox import isRunningOnWindows
import datetime
import os
from flask_socketio import SocketIO
from flask import render_template
from brain import controler as controler

current = None


def log(message):
    global current
    current.info(message)


def debug(message):
    global current
    current.debug(message)


def info(message):
    global current
    current.info(message)


def warning(message):
    global current
    current.warning(message)


def error(message):
    global current
    current.error(message)


class Server:
    def __init__(self):
        global current
        self.controler = controler.Controler("config.json")
        self.botName = self.controler.config["botname"]
        self.lastPicture = "/static/img/terminator_penguin.png"
        self.lastPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.isRunningOnWindows = isRunningOnWindows()
        root = ""
        if not self.isRunningOnWindows:
            root = "/terminator"
        self.writePicturePath = os.getcwd() + root + "/face/webserver/static/img/cam/"
        self.app = None
        self.socketio = None
        self.notifications = []
        self.notifications_count = 0
        self.console_messages = []
        self.console_messages_count = 0
        self.app_is_running = False
        self.page_title = "vide"
        self.active_tasks = 0
        current = self
        log("-------------------------------webserver Initialized----------------------------------")

    def set_last_picture(self, filename):
        self.lastPicture = self.readPicturePath+filename
        self.lastPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath+filename))

    def start(self):
        log("----------------------------importing webserver config---------------------------------")
        from face import webserver
        log("------------------------------starting webserver-------------------------------------")
        app = self.app
        #self.display_state()
        self.app_is_running = True
        self.socketio.run(app, debug=self.controler.config["server_debug"], port=self.controler.config["server_port"],
                          host=self.controler.config["server_host"], use_reloader=False)

    def display_state(self):
        message = "--------------------------------Current server config--------------------------------<br/>"
        message = message + "*************************************************************************************<br/>"
        message = message + "Name : {}".format(self.botName) + "<br/>"
        message = message + "lastPicture : {}".format(self.lastPicture) + "<br/>"
        message = message + "lastPictureDateTime : {}".format(self.lastPictureDateTime) + "<br/>"
        message = message + "readPicturePath : {}".format(self.readPicturePath) + "<br/>"
        message = message + "self.writePicturePath : {}".format(self.writePicturePath) + "<br/>"
        message = message + "isRunningOnWindows : {}".format(self.isRunningOnWindows) + "<br/>"
        message = message + "app.root_path: " + self.app.root_path + "<br/>"
        message = message + "app.instance_path: " + self.app.instance_path + "<br/>"
        message = message + "app: " + str(self.app) + "<br/>"
        message = message + "app_is_running:" + str(self.app_is_running) + "<br/>"
        message = message + "notifications: " + str(self.notifications) + "<br/>"
        message = message + "nb console messages: " + str(self.console_messages_count) + "<br/>"
        message = message + "*************************************************************************************<br/>"
        self.debug(message)

    def create_info_notification(self, text):
        self.add_notification(create_info(text))

    def create_error_notification(self, text):
        self.add_notification(create_error(text))

    def create_warning_notification(self, text):
        self.add_notification(create_warning(text))

    def add_notification(self, n):
        self.notifications.append(n)
        self.notifications_count = len(self.notifications)
        self.info("new notification added: " + str(n.type) + " -- " + n.message)
        html = render_template("common/templates/notifications.html", config=self)
        self.socketio.emit('broadcasted notifications', html)

    def delete_notification(self, i):
        self.notifications.pop(i)
        self.notifications_count = len(self.notifications)
        html = render_template("common/templates/notifications.html", config=self)
        self.socketio.emit('broadcasted notifications', html)

    def insert_console_message(self, console_message):
        self.console_messages.insert(0, console_message)
        self.console_messages_count = len(self.console_messages)
        if self.app_is_running:
            html = render_template("public/view_logs/logs_line.html", it=console_message)
            self.socketio.emit('broadcasted console message', html)

    def debug(self, message):
        self.insert_console_message(cm.debug(message))

    def info(self, message):
        self.insert_console_message(cm.info(message))

    def warning(self, message):
        self.insert_console_message(cm.warning(message))

    def error(self, message):
        self.insert_console_message(cm.error(message))



