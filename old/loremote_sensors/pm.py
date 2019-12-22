import traceback

import RPi.GPIO as gpio
import serial

from loremote_sensors.config import pmsensor_port
from loremote_sensors.dto import PmMeasurement

NUMBER_OF_READS = 3
RETRIES = 3


class PmSensorFacade(object):
    def __init__(self):
        self.sensor_terminal = None

    def get_pm_reading(self, attempt=0):
        try:
            self.sensor_terminal = serial.Serial(pmsensor_port, 9600)
            measurements = self.__get_measurements__()
            return PmMeasurement(measurements[0], measurements[1])
        except Exception as e:
            if attempt >= RETRIES:
                raise e
            else:
                return self.get_pm_reading(attempt=attempt+1)

    def __get_measurements__(self):
        readings = [__read_measurements_from_sensor__(
            self.sensor_terminal) for i in range(NUMBER_OF_READS)]
        avgs = tuple(map(lambda y: sum(y) / float(len(y)), zip(*readings)))
        return avgs[0], avgs[1]


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
