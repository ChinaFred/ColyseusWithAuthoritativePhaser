import brain.config as config
from face import webserver


def start():
    print("------------------------------starting webserver-------------------------------------")
    config.current.app.run(debug=True, port=80, host='0.0.0.0')

