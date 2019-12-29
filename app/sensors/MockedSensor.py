from app.sensors.Sensor import Sensor
from app.shared.measurement import Measurement


class MockedSensor(Sensor):
    def __init__(self, sensor_name: str):
        self.sensor_name = sensor_name

    def measure(self):
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name="temperature", value=22.0, unit="C")
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name="humidity", value=50.0, unit="%")
        return [temperature, humidity]
