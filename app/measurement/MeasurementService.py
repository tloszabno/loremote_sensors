class MeasurementService(object):
    def __init__(self, sensors=[], repositories=[]):
        self.sensors = sensors
        self.repositories = repositories

    def measure(self):
        all_measurements = []
        for sensor in self.sensors:
            all_measurements += sensor.measure()
        for repository in self.repositories:
            repository.save(all_measurements)
