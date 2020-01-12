# coding: utf-8
import RPi.GPIO as GPIO
import time


# vertical positions
V_POS_CENTER = 6
V_POS_TOP = 1
V_POS_BOTTOM = 10
# Horizontal positions
H_POS_MIN = 2
H_POS_MAX = 6
H_POS_CENTER = 6


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
        time.sleep(1)


print("s")
s = ServoMotor(22)
s.go_to_position(V_POS_CENTER)
s.go_to_position(V_POS_TOP)
s.go_to_position(V_POS_BOTTOM)

print("h")
h = ServoMotor(27)
h.go_to_position(H_POS_CENTER)
h.go_to_position(H_POS_MIN)
h.go_to_position(H_POS_MAX)

s.go_to_position(V_POS_CENTER)
h.go_to_position(H_POS_CENTER)
GPIO.cleanup()


