from flask import render_template
from robot import config
from sensors.camera import test_action

app = config.current.app


@app.route('/ajaxExample', methods=['GET'])
def ajaxExample():
    print("ajax call success")
    print("Taking picture")
    test_action.test_draw_image("monImage.png")
    template = render_template("common/templates/cards/camera_card.html", config=config.current)
    print(template)
    return template
