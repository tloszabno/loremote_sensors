from typing import List

from app.measurement.Measurement import Measurement


class Sensor(object):
    def measure(self) -> List[Measurement]:
        pass
