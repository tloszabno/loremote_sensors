import sys

from app import config
from app.listeners.Listener import LogListener
from app.measurement.MeasurementService import MeasurementService
from app.repositories.DbRepository import DbRepository
from app.scheduler.MeasurementScheduler import MeasurementScheduler
from app.sensors import SensorFactory
from app.web import web_app

repository = DbRepository(config.DB_PATH)
listeners = [LogListener()]


def main(mocked=False):
    sensors = SensorFactory.create_sensors() if not mocked else SensorFactory.create_mocked_sensors()
    measurement_service = MeasurementService(repository=repository, sensors=sensors, listeners=listeners)
    measurement_scheduler = MeasurementScheduler(measurement_service=measurement_service)
    measurement_scheduler.start()
    web_app.run_web_server(repository)


if __name__ == "__main__":
    _mocked_ = (len(sys.argv) > 1 and sys.argv[1] == "--mocked")
    main(mocked=_mocked_)
