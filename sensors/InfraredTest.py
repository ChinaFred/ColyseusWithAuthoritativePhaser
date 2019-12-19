import RPi.GPIO as GPIO

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(DR, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(DL, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        DR_status = GPIO.input(DR)
        DL_status = GPIO.input(DL)
        print("DR_status :" + str(DR_status))
        print("DL_status :" + str(DL_status))


except KeyboardInterrupt:
    GPIO.cleanup()



