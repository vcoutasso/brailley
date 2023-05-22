from .image_filter import ImageFilter
import numpy as np


class MultipleFiltersDecorator(ImageFilter):
    """
    Concrete class representing a decorator for applying multiple image filters.

    This class extends the abstract class ImageFilter and implements the 'apply_filter'
    method to apply multiple image filters.

    Attributes:
        _filters (list[ImageFilter]): List of image filters to be applied.
    """

    _filters: list[ImageFilter]

    def __init__(self, filters: list[ImageFilter]):
        """
        Initialize the MultipleFiltersDecorator with the given filters.

        Args:
            filters (list[ImageFilter]): List of image filters to be applied.

        Returns:
            None

        Raises:
            None
        """
        self._filters = filters

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        """
        Apply multiple image filters to the given image array.

        This method applies each image filter in the _filters list to the given image array, sequentially.
        The output of each filter is used as the input for the next filter, and the final result is returned.

        Args:
            array (np.ndarray): The image array to apply the multiple filters to.

        Returns:
            np.ndarray: The filtered image array after applying all the filters.

        Raises:
            None
        """
        for filter in self._filters:
            array = filter.apply_filter(array)
        return array
