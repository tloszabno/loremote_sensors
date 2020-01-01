from app.sensors.Sensor import Sensor
from app.measurement.Measurement import Measurement, MeasurementTypes, MeasurementUnits


class MockedSensor(Sensor):
    def __init__(self, sensor_name: str):
        self.sensor_name = sensor_name

    def measure(self):
        temperature = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.TEMPERATURE,
                                  value=22.0, unit=MeasurementUnits.TEMPERATURE)
        humidity = Measurement(sensor_name=self.sensor_name, measurement_name=MeasurementTypes.HUMIDITY, value=50.0,
                               unit=MeasurementUnits.HUMIDITY)
        return [temperature, humidity]
