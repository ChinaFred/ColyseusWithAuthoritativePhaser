import threading
import time
import tools.console_message as general
from face.webserver import broadcast_notifications


def test(text):
    general.log("text")
    while True:
        general.log(text)
        time.sleep(20)
        broadcast_notifications()


def test_threads():
    c = threading.Thread(name="notifications", daemon=True, target=test, args="c")
    general.log(threading.active_count())
    c.start()

