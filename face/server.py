# coding: utf-8
import tools.console_message as cm
from tools.notification import create_info, create_error, create_warning
from tools.toolbox import isRunningOnWindows
import datetime
import os
from flask_socketio import SocketIO
from flask import render_template
from brain import controler as controler
import threading
import json

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
        self.config_filename = os.getcwd() + "/config.json"
        self.isRunningOnWindows = isRunningOnWindows()
        root = ""
        self.app = None
        self.socketio = None
        self.controler = None
        with open(self.config_filename) as json_data_file:
            self.config = json.load(json_data_file)
        self.botName = self.config["botname"]
        self.latestPicture = "/static/img/terminator_penguin.png"
        self.latestPictureDateTime = ""
        self.readPicturePath = "/static/img/cam/"
        self.writePicturePath = os.getcwd() + root + "/face/webserver/static/img/cam/"
        self.notifications = []
        self.notifications_count = 0
        self.console_messages = []
        self.console_messages_count = 0
        self.app_is_running = False
        self.page_title = "vide"
        self.active_tasks = 0
        current = self
        log("-------------------------------webserver Initialized----------------------------------")

    def set_latest_picture(self, filename):
        self.latestPicture = self.readPicturePath + filename
        self.latestPictureDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.writePicturePath + filename))

    def start(self):
        log("----------------------------importing webserver config---------------------------------")
        from face import webserver
        app = self.app
        log("------------------------------Enabling actions-------------------------------")
        self.controler = controler.Controler(self)
        log("------------------------------starting webserver-------------------------------------")
        #self.display_state()
        self.app_is_running = True
        self.socketio.run(app, debug=self.config["server_debug"], port=self.config["server_port"],
                          host=self.config["server_host"], use_reloader=False)

    def display_state(self):
        message = "--------------------------------Current server config--------------------------------<br/>"
        message = message + "*************************************************************************************<br/>"
        message = message + "Name : {}".format(self.botName) + "<br/>"
        message = message + "lastPicture : {}".format(self.latestPicture) + "<br/>"
        message = message + "lastPictureDateTime : {}".format(self.latestPictureDateTime) + "<br/>"
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

    @staticmethod
    def get_nb_active_tasks():
        return threading.active_count()

    def display_active_threads(self):
        message = "--------------------------------Current server threads--------------------------------<br/>"
        message = message + "*************************************************************************************<br/>"
        message = message + "Threads count : " + str(self.get_nb_active_tasks()) + "<br/>"
        for thread in threading.enumerate():
            message = message + ('Thread (name: "{0}")<br/>'.format(thread.name))
        message = message + "*************************************************************************************<br/>"
        self.debug(message)

    def display_active_tasks(self):
        message = "--------------------------------Current server tasks---------------------------------<br/>"
        message = message + "*************************************************************************************<br/>"
        active_tasks = self.controler.get_active_tasks()
        message = message + "Tasks count : " + str(len(active_tasks)) + "<br/>"
        for a in active_tasks:
            message = message + ('Tâche: "<strong>{0}</strong> ({1})"<br/>'.format(a.name, a.threadName))
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
        html = render_template("common/templates/notifications.html", server=self)
        self.socketio.emit('broadcasted notifications', html)

    def delete_notification(self, i):
        self.notifications.pop(i)
        self.notifications_count = len(self.notifications)
        html = render_template("common/templates/notifications.html", server=self)
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



