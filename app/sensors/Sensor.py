from typing import List

from app.shared.measurement import Measurement


class Sensor(object):
    def measure(self) -> List[Measurement]:
        pass
