import sys

from app.sensors.Sensor import Sensor

import serial
import traceback
from app.measurement.Measurement import Measurement, MeasurementUnits

NUMBER_OF_READS = 3
RETRIES = 3


class PmSensor(Sensor):
    def __init__(self, sensor_name: str, port: str):
        self.sensor_terminal = None
        self.sensor_name = sensor_name
        self.port = port

    def measure(self, attempt=0):
        pm10_value, pm25_value, error = 0.0, 0.0, ""
        try:
            self.sensor_terminal = serial.Serial(self.port, 9600)
            measurements = self.__get_measurements__()
            pm10_value = float(measurements[0])
            pm25_value = float(measurements[1])
        except Exception as e:
            if attempt >= RETRIES:
                error = str(e)
                traceback.print_stack(file=sys.stderr)
            else:
                return self.measure(attempt=attempt + 1)
        pm10 = Measurement(sensor_name=self.sensor_name, measurement_name="pm_10", value=pm10_value,
                           unit=MeasurementUnits.AIR_POLLUTION, error=error)
        pm25 = Measurement(sensor_name=self.sensor_name, measurement_name="pm_2.5", value=pm25_value,
                           unit=MeasurementUnits.AIR_POLLUTION, error=error)
        return [pm10, pm25]

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
