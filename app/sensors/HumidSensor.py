from app.sensors.Sensor import Sensor
from app.measurement.Measurement import Measurement

NUMBER_OF_READS = 3
RETRIES = 3


class HumidSensor(Sensor):
    def __init__(self, sensor_name: str, port: int):
        self.sensor_name = sensor_name
        self.port = port

    def measure(self):
        readings = [self.__get_readings_with_retry__(self.port) for _ in range(NUMBER_OF_READS)]
        avgs = tuple(map(lambda y: sum(y) / float(len(y)), zip(*readings)))
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name="temperature", value=float(avgs[1]),
                                  unit="C")
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name="humidity", value=float(avgs[0]),
                               unit="%")
        return [temperature, humidity]

    def __get_readings_with_retry__(self, port, attempt=0):
        try:
            import Adafruit_DHT
            return Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, port)
        except Exception as e:
            if attempt >= RETRIES:
                temperature = Measurement(sensor_name=self.sensor_name, measurement_name="temperature",
                                          error=str(e),
                                          unit="C")
                humidity = Measurement(sensor_name=self.sensor_name, measurement_name="humidity",
                                       error=str(e),
                                       unit="%")
                return [temperature, humidity]
            else:
                return self.__get_readings_with_retry__(port=port, attempt=attempt + 1)
