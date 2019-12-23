NOTIFICATION_TYPE_INFO = 0
NOTIFICATION_TYPE_WARNING = 1
NOTIFICATION_TYPE_ERROR = 2


class Notification:
    def __init__(self, t, message):
        self.message = message
        self.type = t


def create_error(message):
    return Notification(NOTIFICATION_TYPE_ERROR, message)


def create_info(message):
    return Notification(NOTIFICATION_TYPE_INFO, message)


def create_warning(message):
    return Notification(NOTIFICATION_TYPE_WARNING, message)

