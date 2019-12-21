import sys
import logging



def isRunningOnWindows():
    if sys.platform.find("linux"):
        ret = True
    else:
        ret = False
    return ret


def log(message):
    f = "%(asctime)s: (%(threadName)-9s) %(message)s"
    logging.basicConfig(format=f, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info(message)
