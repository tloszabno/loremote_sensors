import unittest

from hamcrest import assert_that, only_contains
from mockito import mock

from app.repositories.CachedRepository import CachedRepository


class TestCachedRepository(unittest.TestCase):

    def test_it_should_shrink_after_more_than_150_percent_of_initial_size(self):
        # given
        repository = CachedRepository([mock(), mock(), mock()])
        element1 = mock()
        element2 = mock()
        element3 = mock()

        # when
        repository.save(element1)
        repository.save(element2)
        repository.save(element3)

        # then
        assert_that(repository.cache, only_contains(element1, element2, element3))
