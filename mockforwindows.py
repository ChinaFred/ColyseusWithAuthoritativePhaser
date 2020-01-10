from tools.toolbox import *



if isRunningOnWindows():
    print("is running on windows")
    # Replace libraries by fake ones
    import sys
    import fake_rpi

    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)
    import RPI.GPIO as GPIO
    print("end test")