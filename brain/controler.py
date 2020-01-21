# coding: utf-8
import json
from sensors.proximity_detection_sensor import proximity_detection_sensor as pds
from sensors.infrared_remote_control import infrared_remote_control as ir_control
from sensors.camera import camera as cam
# from body.servo import servomotor as sm
from brain.task import *

pds_left = 0
pds_right = 1
sm_horizontal = 0
sm_vertical = 1


class Controler:
    def __init__(self, server):
        # init the elements
        self.pds = [pds.ProximityDetectionSensor(server.config["proximity_left_PIN"]),
                    pds.ProximityDetectionSensor(server.config["proximity_right_PIN"])]
        self.camera = cam.Camera()
        # self.ir_control = ir_control.InfraredRemoteControl(server.config["IR_control_PIN"], server.socketio.sleep)
        # self.servos = [sm.init_horizontal_servo(server.config["servo_motor_horizontal_PIN"]),
                       # sm.init_vertical_servo(server.config["servo_motor_vertical_PIN"])]
        # results and statuses
        self.pds_statuses = [0, 0]
        self.ir_commands = []
        # actions
        self.tasks = []
        self.init_tasks(server)

    def init_tasks(self, server):
        self.tasks.append(Task.init_read_continuously_pds_statuses_task())
        self.tasks.append(Task.init_read_continuously_ir_remote_control_task())
        self.tasks.append(Task.init_shoot_photo())
        self.tasks.append(Task.init_stream_video())

    def get_action(self, task_name):
        ret = None
        for a in self.tasks:
            if a.name == task_name:
                ret = a
                break
        return ret

    def count_active_tasks(self):
        count = 0
        for a in self.tasks:
            if a.status == TaskStatus.RUNNING:
                count = count + 1
        return count

    def get_active_tasks(self):
        ret = []
        for a in self.tasks:
            if a.status == TaskStatus.RUNNING:
                ret.append(a)
        return ret

    def add_ir_commands(self, key):
        MAX_COMMANDS = 20
        self.ir_commands.append(key)
        if len(self.ir_commands) > MAX_COMMANDS:
            self.ir_commands.pop(0)

    def pop_first_ir_command(self):
        return self.ir_commands.pop(0)

    def read_latest_ir_command(self):
        return self.ir_commands[len(self.ir_commands)-1]

    def display(self):
        debug("------------------------------------controler----------------------------------------")
        debug("*************************************************************************************")
        debug("*************************************************************************************")

    def read_pds_statuses(self):
        return [self.pds[pds_left].get_status(), self.pds[pds_right].get_status()]









    #import json
    #with open('config.json', 'w') as outfile:
    #    json.dump(data, outfile)