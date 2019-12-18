import robot.config as config
from robot import webserver


def start():
    config.display()
    config.current.app.run()
    print("---------------------------------server started--------------------------------------")


if __name__ == "__main__":
    start()

