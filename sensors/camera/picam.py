import time
import picamera
from robot import config


def shoot_photo(filename):
    with picamera.PiCamera() as camera:
        print("take a picture")
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(config.current.writePicturePath + filename)
        config.current.set_lastPicture(filename)
