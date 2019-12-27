from flask import render_template, request
import face.server as s


app = s.current.app
server = s.current


@app.route('/photo_shoot_ajax', methods=['GET'])
def photo_shoot_ajax():
    server.controler.camera.shoot_photo("camera.jpeg", server)
    server.create_info_notification("Une photo a été prise")
    template = render_template("common/templates/cards/photo_card/img_photo_card.html", config=server)
    server.debug(template)
    return template


@app.route('/get_server_state', methods=['GET'])
def get_server_state():
    server.display_state()
    return "success"


@app.route('/remove_notification', methods=['POST'])
def remove_notification():
    server.debug("request get_json " + str(request.get_json(force=True)))
    json = request.get_json(force=True)
    server.debug(json)
    server.delete_notification(int(request.get_json(force=True).get("index")))
    server.debug("notification removed")
    return "Success"


s.info("--------------------------AJAX Views initialized------------------------------------")
