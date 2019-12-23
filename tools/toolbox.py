import sys


def isRunningOnWindows():
    if sys.platform.find("linux"):
        ret = True
    else:
        ret = False
    return ret
