from .image_filter import ImageFilter
import numpy as np
import cv2


class NoiseRemovalFilter(ImageFilter):
    """
    Concrete class representing a noise removal image filter.

    This class extends the abstract class ImageFilter and implements the 'apply_filter'
    method to apply a noise removal filter.

    Attributes:
        None
    """

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        """
        Apply the noise removal filter to the given image array.

        This method applies a noise removal filter to the given image array using the median blur technique.

        Args:
            array (np.ndarray): The image array to apply the noise removal filter to.

        Returns:
            np.ndarray: The filtered image array after noise removal.

        Raises:
            None
        """
        return cv2.medianBlur(array, 5)
