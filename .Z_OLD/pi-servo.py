# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as G
import time
import os

G.setwarnings(True)
# Set the layout for the pin declaration
G.setmode(G.BCM)
# The Raspberry Pi pin 11(GPIO 18) connect to servo signal line(yellow wire)
# Pin 11 send PWM signal to control servo motion
G.setup(22, G.OUT)

# menu info
print("l = move to the left")
print("r = move to the right")
print("m = move to the middle")
print("t = test sequence")
print("q = stop and exit")
l = "l"
r = "r"
m = "m"
t = "t"
q = "q"
while True:
	# Now we will start with a PWM signal at 50Hz at pin 18. 
	# 50Hz should work for many servo very will. If not you can play with the frequency if you like.
	Servo = G.PWM(22, 50)

	# This command sets the left position of the servo
	Servo.start(2.5)

	# Now the program asks for the direction the servo should turn.
	response = input("Selection: ")

	# You can play with the values.
	# 7.5 is in most cases the middle position
	# 12.5 is the value for a 180 degree move to the right
	# 2.5 is the value for a -90 degree move to the left
	if response == "t":
		print("move to the center position:")
		Servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		print("move to the right position:")
		Servo.ChangeDutyCycle(12.5)
		time.sleep(1)
		print("move to the left position:")
		Servo.ChangeDutyCycle(2.5)
		time.sleep(1)
		# this stops the PWM signal
		print("Move back to start position.")
		Servo.stop()

	# direction right
	elif response == "r":

		# how many steps should the move take.
		steps = input("steps (1 - 10): ")
		print(steps, "steps to the right")
		stepslength = 12.5 / int(steps)
		for Counter in range(int(steps)):
			Servo.ChangeDutyCycle(stepslength * (Counter + 1))
			print(stepslength * (Counter + 1))
			time.sleep(0.5)
			
		time.sleep(1)	
		# PWM stop
		print("Move back to start position.")
		Servo.stop()

	# move to the center position
	elif response == "m":
		print("Move back to the center position.")
		Servo.start(7.5)
		time.sleep(1)
		# PWM stop
		print("Move back to start position.")
		Servo.stop()
	
	# move to the left
	elif response == "l":
		print("Move  to the max right position and then to the left position.")
		Servo.start(12.5)
		# how many steps...
		steps = input("steps (1 - 10): ")
		print(steps, "steps to the right")
		stepslength = 12.5 / int(steps)
		for Counter in range(int(steps)):
			Servo.ChangeDutyCycle(12.5 - (stepslength * (Counter + 1)))
			print (12.5 - (stepslength * (Counter + 1)))
			time.sleep(0.5)
		
		time.sleep(1)
		# PWM stop
		print("Move back to start position.")
		Servo.stop()
	
	# close program
	elif response == "q":
		print("stop the program and exit......")
		Servo.stop()
		G.cleanup()
		exit()
		
	# input not valid
	else:
		print("input not valid!")
