# coding: utf-8
import time
from datetime import datetime
import flask_socketio as sio
from flask import render_template
import tools.toolbox
import random
from brain.task import *


class TaskStatus:
    STOPPED = 0
    RUNNING = 1


class PossibleTasks:
    VOID_TASK = "void task"
    PA_READ_CONTINUOUSLY_PDS_STATUS = "Read proximity sensors"
    PA_READ_CONTINUOUSLY_IR_REMOTE_CONTROL = "Read infrared remote control"
    PA_SHOOT_PHOTO = "Shoot a photo"

    @staticmethod
    def read_continuously_pds_statuses(server):
        with server.app.test_request_context():
            while server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_PDS_STATUS).status == \
                    TaskStatus.RUNNING:
                new_statuses = server.controler.read_pds_statuses()
                if server.controler.pds_statuses != new_statuses:
                    server.controler.pds_statuses = new_statuses
                    html = render_template(
                        "common/templates/cards/proximity_sensors_card/cnt_proximity_sensors_card.html",
                        server=server, PossibleTasks=PossibleTasks)
                    server.socketio.emit('card_update', ["#cnt-proximity", html], broadcast=True)
                time.sleep(0.2)
            Task.broadcast_tasks(server)

    @staticmethod
    def read_continuously_ir_remote_control(server):
        with server.app.test_request_context():
            while server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_IR_REMOTE_CONTROL).status == \
                    TaskStatus.RUNNING:
                new_command = server.controler.ir_control.get_key()
                if  tools.toolbox.isRunningOnWindows():
                    new_command = random.randint(0, 24) # mock pour génération de données
                    server.log("running on windows")
                if new_command is not None: # and new_command != "repeat":
                    server.debug(new_command)
                    server.controler.add_ir_commands(new_command)
                    html = render_template(
                        "common/templates/cards/ir_remote_control_card/cnt_ir_remote_control_card.html",
                        server=server, PossibleTasks=PossibleTasks)
                    server.socketio.emit('card_update', ["#cnt-irrc", html], broadcast=True)
                time.sleep(0.2)
            Task.broadcast_tasks(server)

    @staticmethod
    def shoot_a_photo(server):
        with server.app.test_request_context():
            server.controler.camera.shoot_photo("camera.jpeg", server)
            # server.create_info_notification("Une photo a été prise")
            html = render_template("common/templates/cards/photo_card/img_photo_card.html",
                                   server=server, PossibleTasks=PossibleTasks)
            server.socketio.emit('card_update', ["#img-photo", html], broadcast=True)
            server.debug(html)
            server.controler.get_action(PossibleTasks.PA_SHOOT_PHOTO).stop(server)
            Task.broadcast_tasks(server)

    @staticmethod
    def void_task(actions, server):
        server.error("No action defined")


class Task:
    def __init__(self, name=PossibleTasks.VOID_TASK, function=PossibleTasks.void_task, icon="ti-server"):
        self.name = name
        self.status = TaskStatus.STOPPED
        self.function = function
        self.startedDateTime = None
        self.threadName = None
        self.icon = icon
        # self.id = self.name.replace(' ', '')

    def start(self,  server):
        if self.status == TaskStatus.STOPPED:
            try:
                # server.error(self.id)
                self.status = TaskStatus.RUNNING
                t = server.socketio.start_background_task(self.function, server)
                self.threadName = t.name
                server.info("Task <strong>{0}</strong> ({1}) started".format(self.name, self.threadName))
                self.startedDateTime = datetime.now()
                Task.broadcast_tasks(server)
            except:
                server.error("Failure during task initialization ({0}) ".format(self.name))
                self.status = TaskStatus.STOPPED
        else:
            server.warning("Task <strong>{0}</strong> ({1}) already active".format(self.name, self.threadName))

    def stop(self, server):
        try:
            server.info("Task <strong>{0}</strong> ({1}) will be stopped in a short moment".format(
                self.name, self.threadName))
            self.status = TaskStatus.STOPPED
            self.threadName = None
            self.startedDateTime = None
        except:
            server.error("Failed to stop task {0}".format(self.name))

    @staticmethod
    def init_read_continuously_pds_statuses_task():
        return Task(PossibleTasks.PA_READ_CONTINUOUSLY_PDS_STATUS, PossibleTasks.read_continuously_pds_statuses,
                      "ti-ruler")

    @staticmethod
    def init_read_continuously_ir_remote_control_task():
        return Task(PossibleTasks.PA_READ_CONTINUOUSLY_IR_REMOTE_CONTROL,
                    PossibleTasks.read_continuously_ir_remote_control,
                      "ti-rss-alt")

    @staticmethod
    def init_shoot_photo():
        return Task(PossibleTasks.PA_SHOOT_PHOTO,
                    PossibleTasks.shoot_a_photo,
                      "ti-camera")

    @staticmethod
    def broadcast_tasks(server):
        html = render_template("common/templates/robot_tasks.html", server=server)
        server.socketio.emit('broadcasted_server_tasks', html, broadcast=True)


