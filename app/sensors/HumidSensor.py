import logging
import time

from app.measurement.Measurement import Measurement, MeasurementUnits, MeasurementTypes
from app.sensors.Sensor import Sensor

NUMBER_OF_READS = 4
INTERVAL_BETWEEN_MEASURES_IN_S = 10
RETRIES = 3

logger = logging.getLogger('HumidSensor')


class HumidSensor(Sensor):
    def __init__(self, sensor_name: str, port: int):
        self.sensor_name = sensor_name
        self.port = port

    def measure(self):
        temp_value, humidity_value, error = 0.0, 0.0, ""
        try:
            readings = [self.__get_readings_with_retry__(self.port, i) for i in range(NUMBER_OF_READS)]
            readings = filter(lambda x:  x is not None and x[0] is not None and x[1] is not None, readings)
            avgs = tuple(map(lambda y: sum(y) / float(len(y)), zip(*readings)))
            temp_value = float(avgs[1])
            humidity_value = float(avgs[0])
        except Exception as e:
            error = str(e)
            logger.exception(error)
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.TEMPERATURE,
                                  value=temp_value,
                                  unit=MeasurementUnits.TEMPERATURE, error=error)
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.HUMIDITY,
                               value=humidity_value,
                               unit=MeasurementUnits.HUMIDITY, error=error)
        return [temperature, humidity]

    def __get_readings_with_retry__(self, port, i, attempt=0):
        try:
            if i > 0:
                time.sleep(INTERVAL_BETWEEN_MEASURES_IN_S)
            import Adafruit_DHT
            return Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, port)
        except Exception as e:
            if attempt >= RETRIES:
                raise e
            else:
                return self.__get_readings_with_retry__(port=port, i=i, attempt=attempt + 1)
