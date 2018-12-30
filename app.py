import sys

from loremote_sensors.db import MeasurementsDAO
from loremote_sensors.dto import PmMeasurement


def main(mocked=False):
    if mocked:
        print("Running mocked version")

    dao = MeasurementsDAO()
    dao.save_pm_measurement(PmMeasurement(pm10=10.0, pm2_5=2.5))
    for result in dao.get_last_pm_measurements():
        print(result)


if __name__ == '__main__':
    mocked = len(sys.argv) > 1 and sys.argv[1] == "--mocked"
    main(mocked)
