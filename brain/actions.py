import time
import threading
import flask_socketio as sio
from flask import render_template


STOPPED = 0
RUNNING = 1


class Actions:
    def __init__(self):
        self.threads = []
        self.threads_status = []
        self.index_read_continuously_pds = None

    def read_continuously_pds_statuses(self, s, task_id):
        while self.threads_status[task_id]:
            with s.app.test_request_context():
                new_statuses = s.controler.read_pds_statuses()
                if s.controler.pds_statuses != new_statuses:
                    s.controler.pds_statuses = new_statuses
                    html = render_template(
                        "common/templates/cards/proximity_sensors_card/cnt_proximity_sensors_card.html",
                        config=s)
                    s.socketio.emit('new_pds_statuses', html,  broadcast=True)
                time.sleep(0.2)

    def start_reading_continuously_pds_statuses(self, s):
        if self.index_read_continuously_pds is None:
            self.index_read_continuously_pds = len(self.threads)
            self.threads_status.append(RUNNING)
            self.threads.append(s.socketio.start_background_task(self.read_continuously_pds_statuses,
                                                                 s, self.index_read_continuously_pds
                                                                 ))
        else:
            self.threads_status[self.index_read_continuously_pds] = RUNNING
            self.threads[self.index_read_continuously_pds] = s.socketio.start_background_task(
                                                                    self.read_continuously_pds_statuses,
                                                                    s, self.index_read_continuously_pds
                                                                    )
        s.debug("nombre de tâches actives: %d" % threading.active_count())

    def stop_reading_continuously_pds_statuses(self, s):
        try:
            self.threads_status[self.index_read_continuously_pds] = STOPPED
            s.debug("nombre de tâches actives: %d" % threading.active_count())
        except:
            s.error("Failed to stop task 'reading_continuously_pds_statuses'")



