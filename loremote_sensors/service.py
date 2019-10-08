import sys
import time
import traceback
from threading import Thread
from loremote_sensors.dto import Measurement

import schedule

from loremote_sensors.config import IntervalsConfig


class MeasurementService(object):
    def __init__(self, context):
        self.dao = context.dao
        self.pmSensor = context.pmSensor
        self.humidSensor = context.humidSensor

    def start_periodical_measurements(self):
        self.__configure_measurements__()
        self.__start_background_measurements__()

    def lock_till_end(self):
        if self.thread:
            self.thread.join()

    def __configure_measurements__(self):
        schedule.every(IntervalsConfig.MEASURE_INTERVAL_IN_MIN).minutes.do(self.__measure__)

    def __measure__(self):
        try:
            #todo async:
            humid = self.humidSensor.get_humid_reading()
            pm = self.pmSensor.get_pm_reading()
            measurement = Measurement(pm=pm, humid=humid)
            self.dao.save_measurement(measurement)
        except Exception:
            traceback.print_exc(file=sys.stderr)

    def __start_background_measurements__(self):
        self.thread = Thread(target=self.__scheduler_loop__)
        self.thread.daemon = True
        self.thread.start()

    def __scheduler_loop__(self):
        while self.thread.is_alive():
            schedule.run_pending()
            time.sleep(10)
