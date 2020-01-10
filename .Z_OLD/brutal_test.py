import RPi.GPIO as GPIO


try:
    GPIO.setmode(GPIO.BCM)
    # The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
    # Pin 11 send PWM signal to control servo motion
    print("GPIO 22")
    Servo = GPIO.setup(22, GPIO.OUT)
    Servo = GPIO.PWM(22,  50)
    Servo.start(5)
    Servo.ChangeDutyCycle(2.5)
    GPIO.cleanup()

    print("GPIO 27")
    Servo = GPIO.setup(27, GPIO.OUT)
    Servo = GPIO.PWM(27,  50)
    Servo.start(5)
    Servo.ChangeDutyCycle(2.5)
except(RuntimeError, TypeError, NameError):
    print("foutue erreur " + str(NameError) + ": " + str(RuntimeError))
finally:
    GPIO.cleanup()
