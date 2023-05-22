from .image_filter import ImageFilter
import numpy as np
import cv2


class BinaryFilter(ImageFilter):
    """
    Concrete class representing a binary image filter.

    This class extends the abstract class ImageFilter and implements
    the 'apply_filter' method to apply a binary image filter.

    Attributes:
        None
    """

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        """
        Apply the binary filter to the given image array.

        This method applies a binary image filter to the given image array. It converts the array to grayscale, applies
        thresholding using Otsu's method, and returns the resulting binary array.

        Args:
            array (np.ndarray): The image array to apply the binary filter to.

        Returns:
            np.ndarray: The filtered binary image array.

        Raises:
            None
        """
        try:
            grayscale_array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        except Exception:
            grayscale_array = array
        _, binary_array = cv2.threshold(
            grayscale_array, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )
        return binary_array
