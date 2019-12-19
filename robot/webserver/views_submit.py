from flask import redirect
from robot import config


app = config.current.app


@app.route('/shoot_photo', methods=['POST'])
def shoot_photo():
    print("Taking picture")
    #test_action.test_draw_image("monImage.png")
    return redirect('/')


