import unittest

from mockito import mock, when, verify, arg_that

from app.measurement.MeasurementService import MeasurementService


class TestMeasurementService(unittest.TestCase):

    def setUp(self):
        self.repo1 = mock()
        self.sensor1 = mock()
        self.repo2 = mock()
        self.sensor2 = mock()
        repos = [self.repo1, self.repo2]
        sensors = [self.sensor1, self.sensor2]
        self.service = MeasurementService(repositories=repos, sensors=sensors)

    def test_should_invoke_measure_on_sensors_and_save_in_repositories(self):
        # given
        when(self.sensor1).measure().thenReturn([mock(), mock(), mock()])
        when(self.sensor2).measure().thenReturn([mock(), mock(), mock()])

        # when
        self.service.measure()

        # then
        verify(self.sensor1).measure()
        verify(self.sensor2).measure()

        # and
        verify(self.repo1).save(arg_that(lambda dto: len(dto.values) == 6))
        verify(self.repo2).save(arg_that(lambda dto: len(dto.values) == 6))
