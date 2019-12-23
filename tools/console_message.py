import logging
from datetime import datetime

CONSOLEMESSAGE_TYPE_DEBUG = 0
CONSOLEMESSAGE_TYPE_INFO = 1
CONSOLEMESSAGE_TYPE_WARNING = 2
CONSOLEMESSAGE_TYPE_ERROR = 3


def log(message):
    return info(message)


def direct_logging(message):
    f = "%(asctime)s: (%(threadName)-9s) %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info(message)


def info(message):
    return ConsoleMessage(CONSOLEMESSAGE_TYPE_INFO, str(message))


def warning(message):
    return ConsoleMessage(CONSOLEMESSAGE_TYPE_WARNING, str(message))


def error(message):
    return ConsoleMessage(CONSOLEMESSAGE_TYPE_ERROR, str(message))


def debug(message):
    return ConsoleMessage(CONSOLEMESSAGE_TYPE_DEBUG, str(message))


class ConsoleMessage:
    def __init__(self, t, message):
        self.message = message
        self.type = t
        self.datetime = datetime.now()
        direct_logging(self.message)






