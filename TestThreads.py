import threading
import time
import tools.general as general


def test(text):
    general.log("text")
    while True:
        general.log(text)
        time.sleep(4)


def test_threads():
    a = threading.Thread(name="Gypsy", target=test, args="t")
    b = threading.Thread(name="dsqdsqdqs", daemon=True, target=test, args="p")
    c = threading.Thread(name="Face", daemon=True, target=test, args="c")
    general.log(threading.active_count())
    a.start()
    b.start()
    c.start()

