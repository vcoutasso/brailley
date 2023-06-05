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
            # try to convert to grayscale using numpy as np
            grayscale_array = array.convert('L') # convert to grayscale

        except Exception:
            grayscale_array = array
            thresh = 128
            binary_array = np.where(np.array(grayscale_array).astype('uint8') > thresh, 255, 0)
        return binary_array
