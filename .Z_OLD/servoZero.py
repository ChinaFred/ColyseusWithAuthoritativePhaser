from gpiozero import Servo
from time import sleep

servo = Servo(27)


servo.min()
sleep(2)
servo.mid()
sleep(2)
servo.max()
sleep(2)