import logging

from app.listeners.Listener import Listener
from app.measurement.Measurement import MeasurementsSet, MeasurementTypes

logger = logging.getLogger('TempDifferenceListener')


class TempDifferenceListener(Listener):
    def notify(self, measurement: MeasurementsSet):
        temperatures = measurement.get_all_with_name(MeasurementTypes.TEMPERATURE)
        for i in range(len(temperatures) - 1):
            base_value = temperatures[i].value
            msg = "\n+ Sensor %s has temp=%s, difference with others:\n" % (temperatures[i].sensor_name, str(base_value))
            for j in range(i + 1, len(temperatures)):
                value = temperatures[j].value
                diff = abs(base_value - value)
                factor = base_value / value
                msg += ("\t- Sensor %s has temp=%s\tdifference: %s\tfactor=%s\n" % (
                    temperatures[j].sensor_name, str(value), str(diff), str(factor)))
            logger.warning(msg)
