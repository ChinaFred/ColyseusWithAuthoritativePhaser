# coding: utf-8
from flask import render_template, request
import face.server as s
from brain import actions


app = s.current.app
server = s.current


@app.route('/photo_shoot_ajax', methods=['GET'])
def photo_shoot_ajax():
    server.controler.camera.shoot_photo("camera.jpeg", server)
    server.create_info_notification("Une photo a été prise")
    template = render_template("common/templates/cards/photo_card/img_photo_card.html", config=server)
    server.debug(template)
    return template


@app.route('/read_proximity', methods=['GET'])
def read_proximity():
    server.controler.actions.start_reading_continuously_pds_statuses(server)
    return "success"


@app.route('/stop_proximity', methods=['GET'])
def stop_reading_proximity():
    server.controler.actions.stop_reading_continuously_pds_statuses(server)
    return "success"


@app.route('/get_server_state', methods=['GET'])
def get_server_state():
    server.display_state()
    return "success"


@app.route('/remove_notification', methods=['POST'])
def remove_notification():
    server.delete_notification(int(request.get_json(force=True).get("index")))
    server.debug("notification removed")
    return "Success"


s.info("--------------------------AJAX Views initialized------------------------------------")
