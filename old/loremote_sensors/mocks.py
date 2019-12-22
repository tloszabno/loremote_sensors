from loremote_sensors.dto import PmMeasurement
from loremote_sensors.dto import HumidMeasurement
from loremote_sensors.config import HumidSensor


class MockedPmSensorFacade(object):
    def get_pm_reading(self):
        return PmMeasurement(10.0, 2.5)

class MockedHumidSensorFacade(object):
    def get_humid_reading(self, sensor):
        return HumidMeasurement(28.0, 50) if sensor == HumidSensor.SENSOR_1 else HumidMeasurement(20.0, 50.0)
