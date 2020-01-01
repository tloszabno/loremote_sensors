import logging
from typing import List

from app.measurement.Measurement import Measurement, MeasurementTypes, MeasurementUnits
from app.sensors.Sensor import Sensor

logger = logging.getLogger('BmeSensor')


class BmeSensor(Sensor):
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name

    def measure(self) -> List[Measurement]:
        error, humidity_data, pressure_data, temp_data = self.__measure__()
        temperature = Measurement(sensor_name=self.sensor_name,
                                  measurement_name=MeasurementTypes.TEMPERATURE,
                                  value=temp_data,
                                  unit=MeasurementUnits.TEMPERATURE,
                                  error=error)
        humidity = Measurement(sensor_name=self.sensor_name,
                               measurement_name=MeasurementTypes.HUMIDITY,
                               value=float(humidity_data),
                               unit=MeasurementUnits.HUMIDITY,
                               error=error)
        pressure = Measurement(sensor_name=self.sensor_name,
                               measurement_name=MeasurementTypes.PRESSURE,
                               value=float(pressure_data),
                               unit=MeasurementUnits.PRESSURE,
                               error=error)
        return [temperature, humidity, pressure]

    @staticmethod
    def __measure__():
        temp_data, pressure_data, humidity_data = 0.0, 0.0, 0.0
        error = ""
        try:
            from app.sensors.thirdparty.bme280.bme280 import Bme280, MODE_FORCED
            sensor = Bme280()
            sensor.set_mode(MODE_FORCED)
            temp_data, pressure_data, humidity_data = sensor.get_data()
        except Exception as e:
            error = str(e)
            logger.exception(error)
        return error, humidity_data, pressure_data / 100.0, temp_data
