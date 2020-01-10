import RPi.GPIO as GPIO
import time


print("VERTICAL 27")
servoPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(0)  # Initialization
for i in range(3, 11):
    p.ChangeDutyCycle(i)     # Changes the pulse width to 3 (so moves the servo)
    time.sleep(1)

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM

print("HORIZONTAL 22")
servoPIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

h = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
h.start(0)  # Initialization
for i in range(2, 10):
    h.ChangeDutyCycle(i)     # Changes the pulse width to 3 (so moves the servo)
    time.sleep(1)                 # Wait 1 second
h.stop()

GPIO.cleanup()
