import Adafruit_DHT
import traceback
import loremote_sensors.config as config
from loremote_sensors.dto import HumidMeasurement

NUMBER_OF_READS = 2
RETRIES = 3


class HumidSensorFacade(object):
    def get_humid_reading(self):
        readings = [ self.__get_readings_with_retry__() for i in range(NUMBER_OF_READS) ]
        avgs = tuple(map(lambda y: sum(y) / float(len(y)), zip(*readings)))
        return HumidMeasurement(avgs[1], avgs[0])

    def __get_readings_with_retry__(self, attempt=0):
        try:
            return Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, config.humid_sensor_port)
        except Exception as e:
            if attempt >= RETRIES:
                raise e
            else:
                return self.__get_readings_with_retry__(attempt=attempt+1)
