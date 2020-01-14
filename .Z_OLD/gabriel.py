print ("pouloulou")

# coding: utf-8
import RPi.GPIO as GPIO
import time
from AlphaBot import AlphaBot

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(DR, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(DL, GPIO.IN, GPIO.PUD_UP)

Ab = AlphaBot()

  

for i in range(1, 4):
    print(i)
    print("shsh")
print("bonjour papa ")


DL_status = 1 # 1 signifie pas d'obstacle
while DL_status:
    DL_status = GPIO.input(DL)
    Ab.forward(2)
    print("avance")
    Ab.backward(2)
    print("recule ")
    time.sleep(100)
    Ab.right()
    Ab.forward()



print("quoi? ")