from typing import List

from app.measurement.Measurement import MeasurementsSet
from app.repositories.Repository import Repository


class CachedRepository(Repository):
    def __init__(self, elements):
        self.cache = elements[:]
        self.init_elements_size = len(elements)

    def save(self, measurement: MeasurementsSet):
        self.cache.append(measurement)
        if len(self.cache) * 1.5 > self.init_elements_size:
            self.cache = self.cache[-self.init_elements_size:]

    def get_last(self, max=100) -> List[MeasurementsSet]:
        number_of_elements = len(self.cache)
        number_of_elements = min(number_of_elements, max)
        return self.cache[-number_of_elements:]
