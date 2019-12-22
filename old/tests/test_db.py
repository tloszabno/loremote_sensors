import os
import unittest

from hamcrest import assert_that, has_item

from loremote_sensors.db import MeasurementsDAO
from loremote_sensors.dto import PmMeasurement, HumidMeasurement, Measurement

TEST_DB_PATH = "test_db.sqlite"


class TestDao(unittest.TestCase):

    def setUp(self):
        self.dao = MeasurementsDAO(path=TEST_DB_PATH)

    def tearDown(self):
        os.remove(TEST_DB_PATH)

    def test_should_save_and_get_measurement(self):
        # given
        pm = PmMeasurement(pm10=10.0, pm2_5=2.5)
        humid1 = HumidMeasurement(temperature=50.0, humidity=80)
        humid2 = HumidMeasurement(temperature=51.0, humidity=81)
        measurement = Measurement(pm=pm, humid1=humid1, humid2=humid2)

        # when
        self.dao.save_measurement(measurement)
        saved = self.dao.get_last_measurements(max=1)

        # then
        assert_that(saved, has_item(measurement))
