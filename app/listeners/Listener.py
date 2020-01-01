import logging

from app.measurement.Measurement import MeasurementsSet

logger = logging.getLogger('LogListener')


class Listener(object):
    def notify(self, measurement: MeasurementsSet):
        pass


class LogListener(Listener):
    def notify(self, measurement: MeasurementsSet):
        logger.info("Got Measurements: %s" % str(measurement))
