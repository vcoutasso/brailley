from .image_filter import ImageFilter
import numpy as np



class GrayscaleFilter(ImageFilter):
    """
    Concrete class representing a grayscale image filter.

    This class extends the abstract class ImageFilter and implements the
    'apply_filter' method to apply a grayscale image filter.

    Attributes:
        None
    """

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        """
        Apply the grayscale filter to the given image array.

        This method applies a grayscale image filter to the given image array by converting it to grayscale using the
        BGR to grayscale conversion.

        Args:
            array (np.ndarray): The image array to apply the grayscale filter to.

        Returns:
            np.ndarray: The filtered grayscale image array.

        Raises:
            None
        """
        return self.pillow_to_npy(self.npy_to_pillow(array).convert('L'))
