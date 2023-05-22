from abc import ABC, abstractmethod
from io import BytesIO


class CameraIODevice(ABC):
    """
    Abstract base class representing a camera input/output device.

    This class defines the common interface for camera IO devices. Subclasses must implement
    the 'start_preview' and 'capture' methods.

    Attributes:
        None
    """

    @abstractmethod
    def start_preview(self):
        """
        Start the preview of the camera input/output device.

        This method should be implemented by subclasses to start the preview of the camera IO device.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def capture(self, stream: BytesIO, **kwargs):
        """
        Capture an image using the camera IO device and save it to the specified stream.

        This method should be implemented by subclasses to capture an image using the camera IO device
        and save it to the specified stream.

        Args:
            stream (BytesIO): The stream to save the captured image to.
            **kwargs: Additional keyword arguments for capturing options.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
