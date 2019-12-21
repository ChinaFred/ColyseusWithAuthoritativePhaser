from flask import render_template
from sensors.camera import picam
import face.server as server
import tools.general as general


app = server.current.app


@app.route('/photo_shoot_ajax', methods=['GET'])
def photo_shoot_ajax():
    picam.shoot_photo("camera.jpeg")
    template = render_template("common/templates/cards/camera_card.html", config=server.current)
    return template


general.log("--------------------------AJAX Views initialized------------------------------------")
