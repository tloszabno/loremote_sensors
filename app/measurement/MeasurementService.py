from typing import List

from app.listeners.Listener import Listener
from app.repositories.Repository import Repository
from app.sensors.Sensor import Sensor
from app.measurement.Measurement import MeasurementsSet


class MeasurementService(object):
    def __init__(self, repository: Repository, sensors: List[Sensor] = [], listeners: List[Listener] = []):
        self.sensors = sensors
        self.listeners = listeners
        self.repository = repository

    def measure(self):
        all_measurements = []
        for sensor in self.sensors:
            all_measurements += sensor.measure()
        measurement = MeasurementsSet(all_measurements)
        self.repository.save(measurement)
        for repository in self.listeners:
            repository.notify(measurement)
