from typing import List

from app.measurement.Measurement import MeasurementsSet


class Repository(object):
    def save(self, measurement: MeasurementsSet):
        pass

    def get_last(self, max=100) -> List[MeasurementsSet]:
        pass
