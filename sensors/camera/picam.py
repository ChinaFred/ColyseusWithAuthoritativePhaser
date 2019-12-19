import time
from robot import config
from tools import images
global hasPicam
try:
    hasPicam = True
    import picamera
except:
    hasPicam = False
    print("pas de picam")


def shoot_photo(filename):
    filename = str(time.time()) + filename
    filepath = config.current.writePicturePath + filename
    try:
        if not hasPicam:
            print("draw an hello world picture")
            images.draw_fake_image(filepath)
        else:
            with picamera.PiCamera() as camera:
                print("take a picture")
                camera.resolution = (640, 480)
                camera.start_preview()
                # Camera warm-up time
                time.sleep(2)
                camera.capture(filepath)
        config.current.set_lastPicture(filename)
    except Exception as e:
        print("error in shoot_photo")
        print("filename : " + filename)
        print("filePath : " + filepath)
        print(str(e))
