from .image_filter import ImageFilter
import numpy as np


class MultipleFiltersDecorator(ImageFilter):
    _filters: list[ImageFilter]

    def __init__(self, filters: list[ImageFilter]):
        self._filters = filters

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        for filter in self._filters:
            array = filter.apply_filter(array)
        return array
