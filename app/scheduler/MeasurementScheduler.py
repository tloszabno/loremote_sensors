import sys
import time
import traceback

import schedule
from threading import Thread

from app.config import MEASURE_INTERVAL_IN_MIN
from app.measurement.MeasurementService import MeasurementService


class MeasurementScheduler(object):
    def __init__(self, measurement_service: MeasurementService):
        self.measurement_service = measurement_service
        self.thread = Thread(target=self.__execute_scheduled_measurements__)
        self.thread.daemon = True

    def start(self):
        self.__configure_measurements__()
        self.thread.start()

    def __configure_measurements__(self):
        schedule.every(MEASURE_INTERVAL_IN_MIN).minutes.do(self.__measure__)

    def __measure__(self):
        try:
            self.measurement_service.measure()
        except Exception:
            traceback.print_exc(file=sys.stderr)  # FIXME: add better error handling

    def __execute_scheduled_measurements__(self):
        self.__measure__()
        while self.thread.is_alive():
            schedule.run_pending()
            time.sleep(10)
