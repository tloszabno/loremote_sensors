import uuid
from datetime import datetime

from app.shared.measurement import MeasurementsSet


class MeasurementService(object):
    def __init__(self, sensors=[], repositories=[]):
        self.sensors = sensors
        self.repositories = repositories

    def measure(self):
        all_measurements = []
        for sensor in self.sensors:
            all_measurements += sensor.measure()
        measurement = MeasurementsSet(str(uuid.uuid4()), datetime.now(), all_measurements)
        for repository in self.repositories:
            repository.save(measurement)
