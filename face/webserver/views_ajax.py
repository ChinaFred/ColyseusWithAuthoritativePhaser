# coding: utf-8
from flask import render_template, request
import face.server as s
from brain.task import *


app = s.current.app
server = s.current


@app.route('/toggle_task_state/<task>')
def toggle_task_state(task):
    try:
        server.info("Starting task '{0}'".format(task))
        action = server.controler.get_action(task)
        if action.status == TaskStatus.STOPPED:
            action.start(server)
        else:
            action.stop(server)
    except:
        server.error("Error while trying to toggle task ({0}) state.".format(task))
    return "success"

@app.route('/photo_shoot_ajax', methods=['GET'])
def photo_shoot_ajax():
    server.controler.get_action(PossibleTasks.PA_SHOOT_PHOTO).start(server)
    return "success"


@app.route('/read_proximity', methods=['GET'])
def read_proximity():
    server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_PDS_STATUS).start(server)
    return "success"


@app.route('/stop_proximity', methods=['GET'])
def stop_reading_proximity():
    server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_PDS_STATUS).stop(server)
    return "success"


@app.route('/read_irrc', methods=['GET'])
def read_irrc():
    server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_IR_REMOTE_CONTROL).start(server)
    return "success"


@app.route('/stop_irrc', methods=['GET'])
def stop_reading_irrc():
    server.controler.get_action(PossibleTasks.PA_READ_CONTINUOUSLY_IR_REMOTE_CONTROL).stop(server)
    return "success"


@app.route('/get_server_state', methods=['GET'])
def get_server_state():
    server.display_state()
    return "success"


@app.route('/get_server_tasks', methods=['GET'])
def get_server_tasks():
    server.display_active_tasks()
    return "success"


@app.route('/get_server_threads', methods=['GET'])
def get_server_threads():
    server.display_active_threads()
    return "success"


@app.route('/remove_notification', methods=['POST'])
def remove_notification():
    server.delete_notification(int(request.get_json(force=True).get("index")))
    server.debug("notification removed")
    return "Success"


s.info("--------------------------AJAX Views initialized------------------------------------")
