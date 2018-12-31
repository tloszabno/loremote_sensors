from loremote_sensors.dto import PmMeasurement


class MockedPmSensorFacade(object):
    def get_pm_reading(self):
        return PmMeasurement(10.0, 2.5)
