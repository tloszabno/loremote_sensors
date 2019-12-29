from app.shared.measurement import MeasurementsSet


class Listener(object):
    def notify(self, measurement: MeasurementsSet):
        pass


class LogListener(Listener):
    def notify(self, measurement: MeasurementsSet):
        print("Got Measurements: %s" % str(measurement))
