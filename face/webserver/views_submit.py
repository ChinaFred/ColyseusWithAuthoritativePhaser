from flask import redirect
import face.server as server
from face.server import log


app = server.current.app


@app.route('/shoot_photo', methods=['POST'])
def shoot_photo():
    log("Taking a picture")
    #test_action.test_draw_image("monImage.png")
    return redirect('/')


log("-----------------------Submit  Views initialized------------------------------------")

