from loremote_sensors.context import Context
from loremote_sensors.service import MeasurementService
from loremote_sensors.web_app import run_web_server


def main(mocked=False):
    context = Context(mocked)
    service = MeasurementService(context)
    service.start_periodical_measurements()
    run_web_server(context)
