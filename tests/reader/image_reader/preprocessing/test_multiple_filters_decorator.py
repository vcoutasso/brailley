from brailley.reader.image_reader.preprocessing.multiple_filters_decorator import (
    MultipleFiltersDecorator,
)
from brailley.reader.image_reader.preprocessing.image_filter import ImageFilter
from unittest.mock import Mock
from unittest import TestCase
import numpy as np


class TestMultipleFiltersDecorator(TestCase):
    def test_apply_filter_shouldNotModifyImage_whenFiltersArrayIsEmpty(self):
        input = np.arange(16).reshape(4, 4)

        sut = MultipleFiltersDecorator(filters=[])
        output = sut.apply_filter(input)

        self.assertTrue(np.array_equal(input, output))

    def test_apply_filter_shouldCallEveryFilterOnce(self):
        input = np.arange(16).reshape(4, 4)

        mockFilter1 = Mock()
        mockFilter2 = Mock()
        mockFilter3 = Mock()

        sut = MultipleFiltersDecorator(filters=[mockFilter1, mockFilter2, mockFilter3])
        sut.apply_filter(input)

        mockFilter1.apply_filter.assert_called_once()
        mockFilter2.apply_filter.assert_called_once()
        mockFilter3.apply_filter.assert_called_once()

    def test_apply_filter_shouldYieldSameResultOfIndividualFilters(self):
        input = np.arange(16).reshape(4, 4)

        filter1 = MultiplyByTwoFilter()
        filter2 = NegateFilter()

        expected_output = filter2.apply_filter(filter1.apply_filter(input))

        sut = MultipleFiltersDecorator(filters=[filter1, filter2])
        output = sut.apply_filter(input)

        self.assertTrue(np.array_equal(output, expected_output))


class MultiplyByTwoFilter(ImageFilter):
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        return 2 * array


class NegateFilter(ImageFilter):
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        return -1 * array
