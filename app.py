import sys

from app import config
from app.measurement.MeasurementService import MeasurementService
from app.repositories.DbRepository import DbRepository
from app.scheduler.MeasurementScheduler import MeasurementScheduler
from app.sensors import SensorFactory

repository = DbRepository(config.DB_PATH)


def main(mocked=False):
    sensors = SensorFactory.create_sensors() if not mocked else SensorFactory.create_mocked_sensors()
    measurement_service = MeasurementService(repository=repository, sensors=sensors)
    measurement_scheduler = MeasurementScheduler(measurement_service=measurement_service)
    measurement_scheduler: measurement_scheduler


if __name__ == "__main__":
    _mocked_ = (len(sys.argv) > 1 and sys.argv[1] == "--mocked")
    main(mocked=_mocked_)
