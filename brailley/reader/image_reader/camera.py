from abc import ABC, abstractmethod
from PIL.Image import Image


class Camera(ABC):
    """
    Abstract base class representing a camera.

    This class defines the common interface for cameras. Subclasses must implement the 'capture' method.

    Attributes:
        None
    """

    @abstractmethod
    def capture(self) -> Image:
        """
        Capture an image using the camera.

        This method should be implemented by subclasses to capture an image using the specific camera implementation.

        Returns:
            Image: The captured image as a PIL Image object.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
