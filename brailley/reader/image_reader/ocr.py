from abc import ABC, abstractmethod
from PIL.Image import Image


class OCR(ABC):
    """
    Abstract base class representing an OCR (Optical Character Recognition) system.

    This class defines the common interface for OCR systems. Subclasses must implement the 'image_to_string' method.

    Attributes:
        None
    """

    @abstractmethod
    def image_to_string(self, image: Image) -> str:
        """
        Extract text from the given image using OCR.

        This method should be implemented by subclasses to extract text from the given image using OCR.

        Args:
            image (Image): The image to perform OCR on.

        Returns:
            str: The extracted text from the image.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
