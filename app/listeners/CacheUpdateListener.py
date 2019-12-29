from app.listeners.Listener import Listener
from app.measurement.Measurement import MeasurementsSet
from app.repositories.CachedRepository import CachedRepository


class CacheUpdateListener(Listener):
    def __init__(self, cache: CachedRepository):
        self.cache = cache

    def notify(self, measurement: MeasurementsSet):
        self.cache.save(measurement)