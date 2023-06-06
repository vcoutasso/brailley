from abc import ABC, abstractmethod
from PIL import Image as Img
from PIL.Image import Image
import numpy as np



class ImageFilter(ABC):
    """
    Abstract base class for image filters.

    This class defines the common interface for image filters. Subclasses must implement the 'apply_filter' method.

    Attributes:
        None
    """

    @abstractmethod
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        """
        Apply the image filter to the given image array.

        This method should be implemented by subclasses to apply the specific image filter algorithm to the image array.

        Args:
            array (np.ndarray): The image array to apply the filter to.

        Returns:
            np.ndarray: The filtered image array.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    def apply(self, image: Image) -> Image:
        """
        Apply the image filter to the given PIL Image.

        This method converts the PIL Image to a NumPy array, applies the image filter using the 'apply_filter' method,
        and converts the filtered array back to a PIL Image.

        Args:
            image (Image): The PIL Image to apply the filter to.

        Returns:
            Image: The filtered PIL Image.

        Raises:
            None
        """
        image_array = self.pillow_to_npy(image)
        filtered_array = self.apply_filter(image_array)
        return self.npy_to_pillow(filtered_array)

    def pillow_to_npy(self, image: Image) -> np.ndarray:
        """
        Convert a PIL Image to a NumPy array.

        This method converts the given PIL Image to a NumPy array.

        Args:
            image (Image): The PIL Image to convert.

        Returns:
            np.ndarray: The converted NumPy array.

        Raises:
            None
        """
        return np.array(image)

    def npy_to_pillow(self, array: np.ndarray) -> Image:
        """
        Convert a NumPy array to a PIL Image.

        This method converts the given NumPy array to a PIL Image.

        Args:
            array (np.ndarray): The NumPy array to convert.

        Returns:
            Image: The converted PIL Image.

        Raises:
            None
        """
        return Img.fromarray(array)
