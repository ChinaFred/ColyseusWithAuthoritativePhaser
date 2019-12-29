import time
from tools import images
try:
    import picamera
    picam_installed = True
except:
    picam_installed = False


class Camera:
    def __init__(self):
        self.picam_installed = picam_installed

    def shoot_photo(self, filename, server, resolution_x=640, resolution_y=480):
        filename = str(time.time()) + filename
        filepath = server.writePicturePath + filename
        try:
            if not self.picam_installed:
                server.warning("draw an hello world picture")
                images.draw_fake_image(filepath)
            else:
                with picamera.PiCamera() as camera:
                    server.info("camera is taking a picture")
                    camera.resolution = (resolution_x, resolution_y)
                    camera.start_preview()
                    # Camera warm-up time
                    time.sleep(2)
                    camera.capture(filepath)
            server.set_last_picture(filename)
        except Exception as e:
            server.error("<h1>error in shoot_photo</h1> </br>filename : " + filename + "</br>filePath : " + filepath +
                         "</br> error : " + str(e))


def stream_video(stream, camera):
    # stream = io.BytesIO()
    # with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording(stream, format='h264', quality=23)

    camera.wait_recording(15)
    camera.stop_recording()
    return camera


def stop_streaming(stream, camera):
    # stream = io.BytesIO()
    # with picamera.PiCamera() as camera:
    camera.stop_recording()
    return camera
