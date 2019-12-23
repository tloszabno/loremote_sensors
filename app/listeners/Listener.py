from app.shared.measurement import MeasurementsSet


class Listener(object):
    def notify(self, measurement: MeasurementsSet):
        pass