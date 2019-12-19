import robot.config as config
from robot import webserver


def start():
    config.display()
    config.current.app.run(debug=True, port=80, host='0.0.0.0')
    print("---------------------------------server started--------------------------------------")


if __name__ == "__main__":
    start()

