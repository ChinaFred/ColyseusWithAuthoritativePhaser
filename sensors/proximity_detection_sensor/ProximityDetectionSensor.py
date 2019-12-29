import RPi.GPIO as GPIO


class ProximityDetectionSensor:
    def __init__(self, pin):
        self.PIN = pin
        GPIO.setup(self.PIN, GPIO.IN)

    def get_status(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        return GPIO.input(self.PIN)



