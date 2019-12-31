from typing import List

from app.measurement.Measurement import Measurement
from app.sensors.Sensor import Sensor


class BmeSensor(Sensor):
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name

    def measure(self) -> List[Measurement]:
        error, humidity_data, pressure_data, temp_data = self.__measure__()
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name="temperature", value=temp_data,
                                  unit="C", error=error)
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name="humidity", value=float(humidity_data),
                               unit="%", error=error)
        pressure = Measurement(sensor_name=self.sensor_name, measurement_name="pressure", value=float(pressure_data),
                               unit="hPa", error=error)
        return [temperature, humidity, pressure]

    @staticmethod
    def __measure__():
        temp_data, pressure_data, humidity_data = 0.0, 0.0, 0.0
        error = ""
        try:
            from app.sensors.thirdparty.bme280 import Bme280, MODE_FORCED
            sensor = Bme280()
            sensor.set_mode(MODE_FORCED)
            temp_data, pressure_data, humidity_data = sensor.get_data()
        except Exception as e:
            error = str(e)
        return error, humidity_data, pressure_data / 100.0, temp_data
