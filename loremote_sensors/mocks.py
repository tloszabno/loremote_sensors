from loremote_sensors.dto import PmMeasurement
from loremote_sensors.dto import HumidMeasurement


class MockedPmSensorFacade(object):
    def get_pm_reading(self):
        return PmMeasurement(10.0, 2.5)
class MockedHumidSensorFacade(object):
    def get_humid_reading(self):
        return HumidMeasurement(28.0, 50)
