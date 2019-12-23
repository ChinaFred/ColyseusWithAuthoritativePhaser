import time
import face.server as s
from tools import images
import tools.console_message as general


server = s.current
try:
    import picamera
    server.hasPiCam = True
except:
    server.hasPiCam = False


def shoot_photo(filename):
    filename = str(time.time()) + filename
    filepath = server.writePicturePath + filename
    try:
        if not server.hasPiCam:
            general.log("draw an hello world picture")
            images.draw_fake_image(filepath)
        else:
            with picamera.PiCamera() as camera:
                general.log("camera is taking a picture")
                camera.resolution = (640, 480)
                camera.start_preview()
                # Camera warm-up time
                time.sleep(2)
                camera.capture(filepath)
        server.set_last_picture(filename)
    except Exception as e:
        general.log("error in shoot_photo")
        general.log("filename : " + filename)
        general.log("filePath : " + filepath)
        general.log(str(e))
