# coding: utf-8

import RPi.GPIO as GPIO
import time


V_POS_MIN = 1
V_POS_MAX = 10
H_POS_MIN = 2
H_POS_MAX = 10


class ServoMotor:
    def __init__(self, pin, min_pos=1, max_pos=10):
        self.frequency = 50
        self.PIN = int(pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(self.PIN, GPIO.OUT)
        print(type(self.PIN))
        GPIO.setup(22, GPIO.OUT)
        print(str( GPIO.PWM(22, 50)))
        self.servo = GPIO.PWM(self.PIN, self.frequency)
        self.servo.start(0)
        # Calibrage
        self.pos_min = min_pos
        self.pos_max = max_pos
        self.pos_current = 0
        self.center()

    # def __del__(self):
    #    self.servo.stop()

    def go_to_position(self, pos):
        self.servo.ChangeDutyCycle(pos)
        time.sleep(1)

    def increase_position(self):
        if self.pos_current < self.pos_max:
            self.pos_current = self.pos_current + 1
        self.go_to_position(self.pos_current)

    def decrease_position(self):
        if self.pos_current > self.pos_min:
            self.pos_current = self.pos_current - 1
        self.go_to_position(self.pos_current)

    def center(self):
        self.servo.ChangeDutyCycle(self.get_center_pos())
        self.pos_current = self.get_center_pos()

    def get_center_pos(self):
        return (self.pos_max + self.pos_min)//2


def init_vertical_servo(pin):
    return ServoMotor(pin, V_POS_MIN, V_POS_MAX)


def init_horizontal_servo(pin):
    return ServoMotor(pin, H_POS_MIN, H_POS_MAX)


s = ServoMotor(22)
print(str(s))

