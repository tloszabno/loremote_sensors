import time
import traceback

import RPi.GPIO as gpio
import serial

from loremote_sensors.config import ports_config, pmsensor_port

NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT = 2
SEEP_TIME_BEFORE_MEASUREMENT_OF_PM_IN_SEC = 30


class PmSensorFacade(object):
    def __init__(self):
        self.sensor_terminal = None

    def get_pm_reading(self):
        __turn_on_sensor__()
        try:
            time.sleep(SEEP_TIME_BEFORE_MEASUREMENT_OF_PM_IN_SEC)
            self.sensor_terminal = serial.Serial(pmsensor_port, 9600)
            return self.__get_measurements__()
        except Exception:
            print(str(traceback.format_exc()))
        finally:
            __turn_of_sensor__()

    def __get_measurements__(self):
        for i in range(NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT):
            __read_measurements_from_sensor__(self.sensor_terminal)
            time.sleep(1)
        return __read_measurements_from_sensor__(self.sensor_terminal)


def __turn_of_sensor__():
    gpio.output(ports_config["pmsensor_switch"], False)


def __turn_on_sensor__():
    gpio.output(ports_config["pmsensor_switch"], True)


def __read_measurements_from_sensor__(terminal):
    def hex_show(argv):
        result = ''
        hLen = len(argv)
        for i in range(hLen):
            hvol = ord(argv[i])
            hhex = '%02x' % hvol
            result += hhex + ' '

    terminal.flushInput()
    retstr = terminal.read(10)
    hex_show(retstr)
    if len(retstr) == 10:
        if retstr[0] == b"\xaa" and retstr[1] == b'\xc0':
            checksum = 0
            for i in range(6):
                checksum = checksum + ord(retstr[2 + i])
            if checksum % 256 == ord(retstr[8]):
                pm25 = ord(retstr[2]) + ord(retstr[3]) * 256
                pm10 = ord(retstr[4]) + ord(retstr[5]) * 256
                return pm10 / 10.0, pm25 / 10.0
    return 0.0, 0.0
