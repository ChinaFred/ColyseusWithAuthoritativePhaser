import RPi.GPIO as GPIO
import time

print("HORIZONTAL 22")
servoPIN = 23
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(0)  # Initialization
p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
time.sleep(1)                 # Wait 1 second
p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
time.sleep(1)

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()
print("VERTICAL 27")
servoPIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(0)  # Initialization
p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
time.sleep(1)                 # Wait 1 second
p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
time.sleep(1)

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()
