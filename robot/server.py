import robot.config as config
from robot import webserver


def start():
    print("---------------------------------server started--------------------------------------")
    config.display()
    print("app.root_path: " + config.current.app.root_path)
    print("app.instance_path: "+config.current.app.instance_path)
    config.current.app.run(debug=True, port=80, host='0.0.0.0')


if __name__ == "__main__":
    start()

