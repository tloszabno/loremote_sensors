from loremote_sensors.db import MeasurementsDAO


class Context(object):
    def __init__(self, mocked):
        self.dao = MeasurementsDAO()
        if mocked:
            print("Creating mocked context")
            from loremote_sensors.mocks import MockedPmSensorFacade
            self.pmSensor = MockedPmSensorFacade()
        else:
            from loremote_sensors.pm import PmSensorFacade
            self.pmSensor = PmSensorFacade()
