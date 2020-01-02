# coding: utf-8
import RPi.GPIO as GPIO


class ServoMotor:
    def __init__(self, pin):
        self.PIN = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(self.PIN, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.servo.start(0)

    def __del__(self):
        self.servo.stop()

    def go_to_position(self, pos):
        self.servo.ChangeDutyCycle(pos)


s = ServoMotor(22)
s.go_to_position(8)


