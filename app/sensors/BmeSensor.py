from typing import List

from app.measurement.Measurement import Measurement
from app.sensors.Sensor import Sensor


class BmeSensor(Sensor):
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name

    def measure(self) -> List[Measurement]:
        from app.sensors.thirdparty.bme280 import Bme280, MODE_FORCED
        sensor = Bme280()
        sensor.set_mode(MODE_FORCED)
        temp_data, pressure_data, humidity_data = sensor.get_data()
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name="temperature", value=temp_data,
                                  unit="C")
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name="humidity", value=float(humidity_data),
                               unit="%")
        pressure = Measurement(sensor_name=self.sensor_name, measurement_name="pressure", value=float(pressure_data),
                               unit="%")
        return [temperature, humidity, pressure]
