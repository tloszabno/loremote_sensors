import Adafruit_DHT
import traceback
import loremote_sensors.config as config
from loremote_sensors.dto import HumidMeasurement

NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT = 2

class HumidSensorFacade(object):
    def get_humid_reading(self):
        try:
            for i in range(1, NUMBER_OF_READS_BEFORE_SAVE_MEASUREMENT):
                Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, config.humid_sensor_port)
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, config.humid_sensor_port)
            return HumidMeasurement(temperature=temperature, humidity=humidity)
        except Exception:
            print(str(traceback.format_exc()))
            #TODO: review exception handling
