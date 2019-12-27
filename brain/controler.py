import json
from sensors.proximity_detection_sensor import ProximityDetectionSensor as pds
from sensors.camera import camera as cam


class Controler:
    def __init__(self, config_filename):
        self.config = None
        with open(config_filename) as json_data_file:
            self.config = json.load(json_data_file)
        self.pds_left = pds.ProximityDetectionSensor(self.config["proximity_left_PIN"])
        self.pds_right = pds.ProximityDetectionSensor(self.config["proximity_right_PIN"])
        self.camera = cam.Camera()
        print("contorler initializes")
        print(self.camera)


    def display(self):
        debug("------------------------------------controler----------------------------------------")
        debug("*************************************************************************************")
        debug("*************************************************************************************")







    #import json
    #with open('config.json', 'w') as outfile:
    #    json.dump(data, outfile)