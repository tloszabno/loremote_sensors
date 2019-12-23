import unittest

from mockito import mock, when, verify, arg_that

from app.measurement.MeasurementService import MeasurementService


class TestMeasurementService(unittest.TestCase):

    def setUp(self):
        self.listener1 = mock()
        self.sensor1 = mock()
        self.listener2 = mock()
        self.sensor2 = mock()
        self.repo = mock()
        listeners = [self.listener1, self.listener2]
        sensors = [self.sensor1, self.sensor2]
        self.service = MeasurementService(repository=self.repo, listeners=listeners, sensors=sensors)

    def test_should_invoke_measure_on_sensors(self):
        # given
        when(self.sensor1).measure().thenReturn([mock(), mock(), mock()])
        when(self.sensor2).measure().thenReturn([mock(), mock(), mock()])

        # when
        self.service.measure()

        # then
        verify(self.sensor1).measure()
        verify(self.sensor2).measure()

    def test_should_save_result_to_repository(self):
        # given
        when(self.sensor1).measure().thenReturn([mock(), mock(), mock()])
        when(self.sensor2).measure().thenReturn([mock(), mock(), mock()])

        # when
        self.service.measure()

        # then
        verify(self.repo).save(arg_that(lambda dto: len(dto.values) == 6))

    def test_should_notify_listeners(self):
        # given
        when(self.sensor1).measure().thenReturn([mock(), mock(), mock()])
        when(self.sensor2).measure().thenReturn([mock(), mock(), mock()])

        # when
        self.service.measure()

        # then
        verify(self.listener1).notify(arg_that(lambda dto: len(dto.values) == 6))
        verify(self.listener2).notify(arg_that(lambda dto: len(dto.values) == 6))
