from loremote_sensors.context import Context
from loremote_sensors.service import MeasurementService


def main(mocked=False):
    context = Context(mocked)
    service = MeasurementService(context)
    service.start_periodical_measurements()
    service.lock_till_end()
