current = None


class Config:
    def __init__(self, botName):
        self.botName = botName
        self.app = None

    def set_app(self, a):
        self.app = a


def init():
    global current
    if current is None:
        print("-------------------------------------------------------------------------------------")
        print("-------------------------------Initializating bot------------------------------------")
        current = Config("Terminator")
    else:
        print("-------------------------------------------------------------------------------------")
        print("-------------------------------Already configured------------------------------------")
    return current


def display():
    global current
    print("*************************************************************************************")
    print("--------------------------------Current config---------------------------------------")
    if current is None:
        print("No configuration defined")

    else:
        print("Name : {}".format(current.botName))
        print("app : {}".format(current.app))
    print("*************************************************************************************")


def set_app(a):
    global current
    current.set_app(a)





