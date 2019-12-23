from flask import render_template, request
from sensors.camera import picam
import face.server as server
from face.server import log
import tools.notification as notification
import time


app = server.current.app


@app.route('/photo_shoot_ajax', methods=['GET'])
def photo_shoot_ajax():
    picam.shoot_photo("camera.jpeg")
    server.current.add_notification(notification.create_info("Une photo a été prise"))
    template = render_template("common/templates/cards/camera_card.html", config=server.current)
    return template


@app.route('/remove_notification', methods=['POST'])
def remove_notification():
    log("request get_json " + str(request.get_json(force=True)))
    json = request.get_json(force=True)
    log(json)
    server.current.delete_notification(int(request.get_json(force=True).get("index")))
    server.error("notification removed")
    return "Success"


log("--------------------------AJAX Views initialized------------------------------------")
