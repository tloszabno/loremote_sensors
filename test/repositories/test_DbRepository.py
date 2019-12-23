import os
import time
import unittest

from hamcrest import assert_that, equal_to

from app.repositories.DbRepository import DbRepository
from app.shared.measurement import MeasurementsSet, Measurement

TEST_DB_PATH = "test_db.sqlite"


class TestDbRepository(unittest.TestCase):

    def setUp(self):
        self.repository = DbRepository(path=TEST_DB_PATH)

    def tearDown(self):
        os.remove(TEST_DB_PATH)

    def test_should_save_and_get_measurement(self):
        # given
        measurement_home_humid = Measurement(sensor_name="home_humid", measurement_name="humidity", value=0.9, unit="%")
        measurement_home_temp = Measurement(sensor_name="home_humid", measurement_name="temperature", value=0.9,
                                            unit="%")
        home_set = MeasurementsSet([measurement_home_humid, measurement_home_temp])

        time.sleep(1)
        measurement_out_humid = Measurement(sensor_name="out_humid", measurement_name="humidity", value=0.9, unit="%")
        measurement_out_temp = Measurement(sensor_name="out_humid", measurement_name="temperature", value=0.9, unit="%")
        out_set = MeasurementsSet([measurement_out_humid, measurement_out_temp])

        # when
        self.repository.save(home_set)
        self.repository.save(out_set)

        # then
        last = self.repository.get_last()
        assert_that(len(last), equal_to(2))
        assert_that(last[0], equal_to(home_set))
        assert_that(last[1], equal_to(out_set))
