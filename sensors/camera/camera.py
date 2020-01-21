# coding: utf-8
import io
import time
from tools import images
import threading
import brain.task as task


try:
    import picamera

    _picam_installed = True
except:
    _picam_installed = False


class Camera:
    frame = None
    last_access = None
    thread = None  # background thread that reads frames from camera
    picam_installed = _picam_installed

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self.read_stream)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def shoot_photo(self, filename, server, resolution_x=640, resolution_y=480):
        filename = str(time.time()) + filename
        filepath = server.writePicturePath + filename
        try:
            if not self.picam_installed:
                images.draw_fake_image(filepath)
                server.debug("waiting to simulate photo processing")
                server.socketio.sleep(5)
            else:
                with picamera.PiCamera() as camera:
                    server.info("camera is taking a picture")
                    camera.resolution = (resolution_x, resolution_y)
                    camera.start_preview()
                    # Camera warm-up time
                    server.socketio.sleep(2)
                    camera.capture(filepath)
            server.set_latest_picture(filename)
        except Exception as e:
            server.error("<h1>error in shoot_photo</h1> </br>filename : " + filename + "</br>filePath : " + filepath +
                         "</br> error : " + str(e))

    @staticmethod
    def get_frame(server):
        Camera.last_access = time.time()
        while Camera.frame is None and server.controler.get_action(task.PossibleTasks.PA_STREAM_VIDEO).status == \
                task.TaskStatus.RUNNING:
            time.sleep(0)
        return Camera.frame

    @staticmethod
    def read_stream(server):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = False

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                Camera.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                print("**************************************PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
                if time.time() - Camera.last_access > 10 or \
                        not server.controler.get_action(task.PossibleTasks.PA_STREAM_VIDEO).status:
                    break
        Camera.thread = None


