import time
import traceback

import RPi.GPIO as gpio
import serial

from loremote_sensors.config import pmsensor_port
from loremote_sensors.dto import PmMeasurement

NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT = 2
SEEP_TIME_BEFORE_MEASUREMENT_OF_PM_IN_SEC = 30

class PmSensorFacade(object):
    def __init__(self):
        self.sensor_terminal = None

    def get_pm_reading(self):
        print("get_pm_reading")
        try:
            self.sensor_terminal = serial.Serial(pmsensor_port, 9600)
            measurements = self.__get_measurements__()
            return PmMeasurement(measurements[0], measurements[1])
        except Exception:
            print(str(traceback.format_exc()))

    def __get_measurements__(self):
        for i in range(NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT):
            __read_measurements_from_sensor__(self.sensor_terminal)
            time.sleep(1)
        return __read_measurements_from_sensor__(self.sensor_terminal)


def __read_measurements_from_sensor__(terminal):
    terminal.flushInput()
    retstr = terminal.read(10)
    if len(retstr) == 10:
        if retstr[0:1] == b"\xaa" and retstr[1:2] == b'\xc0':
            checksum = 0
            for i in range(6):
                checksum = checksum + retstr[2 + i]
            if checksum % 256 == retstr[8]:
                pm25 = retstr[2] + retstr[3] * 256
                pm10 = retstr[4] + retstr[5] * 256
                return pm10 / 10.0, pm25 / 10.0
    return 0.0, 0.0
