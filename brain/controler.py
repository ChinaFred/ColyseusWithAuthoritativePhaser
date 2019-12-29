import json
from sensors.proximity_detection_sensor import ProximityDetectionSensor as PDS
from sensors.camera import camera as cam
from brain.actions import Actions

pds_left = 0
pds_right = 1


class Controler:
    def __init__(self, config_filename):
        self.config = None
        with open(config_filename) as json_data_file:
            self.config = json.load(json_data_file)
        self.pds = [PDS.ProximityDetectionSensor(self.config["proximity_left_PIN"]),
                    PDS.ProximityDetectionSensor(self.config["proximity_right_PIN"])]
        self.camera = cam.Camera()
        self.pds_statuses = [0, 0]
        self.actions = Actions()

    def display(self):
        debug("------------------------------------controler----------------------------------------")
        debug("*************************************************************************************")
        debug("*************************************************************************************")

    def read_pds_statuses(self):
        return [self.pds[pds_left].get_status(), self.pds[pds_right].get_status()]










    #import json
    #with open('config.json', 'w') as outfile:
    #    json.dump(data, outfile)