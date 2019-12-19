from flask import render_template
from robot import config
from sensors.camera import picam

app = config.current.app


@app.route('/ajaxExample', methods=['GET'])
def photo_shoot_ajax():
    picam.shoot_photo("camera.jpeg")
    template = render_template("common/templates/cards/camera_card.html", config=config.current)
    return template
