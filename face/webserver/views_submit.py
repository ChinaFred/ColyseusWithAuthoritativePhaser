from flask import redirect
import face.server as server
import tools.general as general


app = server.current.app


@app.route('/shoot_photo', methods=['POST'])
def shoot_photo():
    print("Taking picture")
    #test_action.test_draw_image("monImage.png")
    return redirect('/')


general.log("-----------------------Submit  Views initialized------------------------------------")

