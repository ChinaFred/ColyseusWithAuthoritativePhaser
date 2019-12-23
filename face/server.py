import tools.console_message as cm
from tools.toolbox import isRunningOnWindows
import threading
import datetime
import time
import os
from flask_socketio import SocketIO
from flask import render_template

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
    def __init__(self, bot_name):
        global current
        self.botName = bot_name
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
        self.display_state()
        self.app_is_running = True
        self.socketio.run(app, debug=True, port=80, host='0.0.0.0', use_reloader=False)

    def display_state(self):
        log("--------------------------------Current server config--------------------------------")
        log("*************************************************************************************")
        log("Name : {}".format(self.botName))
        log("lastPicture : {}".format(self.lastPicture))
        log("lastPictureDateTime : {}".format(self.lastPictureDateTime))
        log("readPicturePath : {}".format(self.readPicturePath))
        log("self.writePicturePath : {}".format(self.writePicturePath))
        log("isRunningOnWindows : {}".format(self.isRunningOnWindows))
        log("app.root_path: " + self.app.root_path)
        log("app.instance_path: " + self.app.instance_path)
        log("app: " + str(self.app))
        log("app_is_running:" + str(self.app_is_running))
        log("notifications: " + str(self.notifications))
        log("nb console messages: " + str(self.console_messages_count))
        log("*************************************************************************************")


    def add_notification(self, n):
        self.notifications.append(n)
        self.notifications_count = len(self.notifications)
        log("new notification added: " + str(n.type) + " -- " + n.message)
        html = render_template("common/templates/notifications.html", config=self)
        self.socketio.emit('broadcasted notifications', html)

    def delete_notification(self, i):
        current.warning("delete_notification at server reached")
        self.notifications.pop(i)
        self.notifications_count = len(self.notifications)
        current.error("notification removed at index :" + str(i))
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



