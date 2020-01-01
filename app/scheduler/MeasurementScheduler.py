import logging
import time
from threading import Thread

import schedule

from app.config import MEASURE_INTERVAL_IN_MIN
from app.measurement.MeasurementService import MeasurementService

logger = logging.getLogger('MeasurementScheduler')


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
            logger.exception("Exception occurred in scheduler module")

    def __execute_scheduled_measurements__(self):
        self.__measure__()
        while self.thread.is_alive():
            schedule.run_pending()
            time.sleep(10)
