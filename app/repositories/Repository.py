from app.shared.measurement import MeasurementsSet


class Repository(object):
    def save(self, measurement: MeasurementsSet):
        pass

    def get_last(self, max=100):
        pass
