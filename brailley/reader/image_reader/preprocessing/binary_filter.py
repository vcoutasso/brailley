from .image_filter import ImageFilter
from PIL.Image import Image
import numpy as np



class BinaryFilter(ImageFilter):
    """
    Concrete class representing a binary image filter.

    This class extends the abstract class ImageFilter and overrides
    the 'apply' method to apply a binary image filter.

    Attributes:
        threshold (Int): binary filter threshold. 64 by default
    """

    threshold = 64

    """
    Apply the binary filter to the given image.

    Args:
        image (Image): The image to apply the binary filter to.

    Returns:
        Image: The filtered binary image.

    Raises:
        None
    """
    def apply(self, image: Image) -> Image:
        return image.convert('L').point(lambda p: 255 if p > self.threshold else 0).convert('1')

    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        raise Exception("Not implemented")
