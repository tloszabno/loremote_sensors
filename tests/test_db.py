import os
import unittest

from hamcrest import assert_that, has_item

from loremote_sensors.db import MeasurementsDAO
from loremote_sensors.dto import PmMeasurement

TEST_DB_PATH = "test_db.sqlite"


class TestDao(unittest.TestCase):

    def setUp(self):
        self.dao = MeasurementsDAO(path=TEST_DB_PATH)

    def tearDown(self):
        os.remove(TEST_DB_PATH)

    def test_should_save_and_get_pm_measurement(self):
        # given
        measurement = PmMeasurement(pm10=10.0, pm2_5=2.5)

        # when
        self.dao.save_pm_measurement(measurement)
        saved = self.dao.get_last_pm_measurements(max=1)

        # then
        assert_that(saved, has_item(measurement))
