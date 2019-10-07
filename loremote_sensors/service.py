import sys
import time
import traceback
from threading import Thread

import schedule

from loremote_sensors.config import IntervalsConfig


class MeasurementService(object):
    def __init__(self, context):
        self.dao = context.dao
        self.pmSensor = context.pmSensor

    def start_periodical_measurements(self):
        self.__configure_measurements__()
        self.__start_background_measurements__()

    def lock_till_end(self):
        if self.thread:
            self.thread.join()

    def __configure_measurements__(self):
        schedule.every(IntervalsConfig.MEASURE_PM_INTERVAL_IN_MIN).minutes.do(self.__measure_pm__)

    def __measure_pm__(self):
        try:
            reading = self.pmSensor.get_pm_reading()
            self.dao.save_pm_measurement(reading)
        except Exception:
            traceback.print_exc(file=sys.stderr)

    def __start_background_measurements__(self):
        print("__start_background_measurements__")
        self.thread = Thread(target=self.__scheduler_loop__)
        self.thread.daemon = True
        self.thread.start()

    def __scheduler_loop__(self):
        while self.thread.is_alive():
            print("run_pending...")
            schedule.run_pending()
            time.sleep(10)
