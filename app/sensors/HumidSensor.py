import sys
import traceback

from app.sensors.Sensor import Sensor
from app.measurement.Measurement import Measurement, MeasurementUnits, MeasurementTypes

NUMBER_OF_READS = 3
RETRIES = 3


class HumidSensor(Sensor):
    def __init__(self, sensor_name: str, port: int):
        self.sensor_name = sensor_name
        self.port = port

    def measure(self):
        temp_value, humidity_value, error = 0.0, 0.0, ""
        try:
            readings = [self.__get_readings_with_retry__(self.port) for _ in range(NUMBER_OF_READS)]
            avgs = tuple(map(lambda y: sum(y) / float(len(y)), zip(*readings)))
            temp_value = float(avgs[1])
            humidity_value = float(avgs[0])
        except Exception as e:
            error = str(e)
            print(str(traceback.format_exc()))
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.TEMPERATURE,
                                  value=temp_value,
                                  unit=MeasurementUnits.TEMPERATURE, error=error)
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.HUMIDITY,
                               value=humidity_value,
                               unit=MeasurementUnits.HUMIDITY, error=error)
        return [temperature, humidity]

    def __get_readings_with_retry__(self, port, attempt=0):
        try:
            import Adafruit_DHT
            read = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, port)
            print("Humid reading: %s" % read)
            return read
        except Exception as e:
            if attempt >= RETRIES:
                raise e
            else:
                return self.__get_readings_with_retry__(port=port, attempt=attempt + 1)
