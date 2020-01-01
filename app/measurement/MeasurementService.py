from typing import List

from app.listeners.Listener import Listener
from app.repositories.Repository import Repository
from app.sensors.Sensor import Sensor
from app.measurement.Measurement import MeasurementsSet
from concurrent.futures import ThreadPoolExecutor


class MeasurementService(object):
    def __init__(self, repository: Repository, sensors: List[Sensor] = [], listeners: List[Listener] = []):
        self.sensors = sensors
        self.listeners = listeners
        self.repository = repository
        self.backgroundExecutor = ThreadPoolExecutor()

    def measure(self):
        all_measurements_futures = []
        for sensor in self.sensors:
            all_measurements_futures += self.backgroundExecutor.submit(sensor.measure)
        all_measurements = [x.result() for x in all_measurements_futures]
        measurement = MeasurementsSet(all_measurements)
        self.repository.save(measurement)
        for repository in self.listeners:
            repository.notify(measurement)
1