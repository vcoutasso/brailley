from .camera_io_device import CameraIODevice
from .flash import Flash
from .camera import Camera
from PIL import Image as Img
from PIL.Image import Image
from io import BytesIO
from time import sleep


class RPICamera(Camera):
    """
    Concrete class representing a camera implementation for Raspberry Pi.

    This class extends the Camera class and provides a camera implementation for Raspberry Pi using a camera IO device.

    Attributes:
        _flash (Flash): The flash used for capturing images.
        _camera (CameraIODevice): The camera IO device for capturing images.
        _stream (BytesIO): The stream used for capturing and storing image data.

    """

    _flash: Flash
    _camera: CameraIODevice
    _stream: BytesIO

    def __init__(self, flash: Flash, camera_io_device: CameraIODevice, warmup: int = 2):
        """
        Initialize the RPICamera with the specified flash, camera IO device, and warm-up time.

        Args:
            flash (Flash): The flash used for capturing images.
            camera_io_device (CameraIODevice): The camera IO device for capturing images.
            warmup (int): The warm-up time in seconds (default: 2).

        Returns:
            None

        Raises:
            None
        """
        self._flash = flash
        self._camera = camera_io_device
        self._stream = BytesIO()
        self._camera.start_preview()
        # camera warm-up
        sleep(warmup)

    def capture(self) -> Image:
        """
        Capture an image using the Raspberry Pi camera.

        This method turns on the flash, captures an image using the camera IO device,
        turns off the flash, and returns the captured image as a PIL Image object.

        Returns:
            Image: The captured image as a PIL Image object.

        Raises:
            None
        """
        self._flash.on()
        self._camera.capture(self._stream, format="jpeg")
        self._flash.off()

        return self._image_from_stream()

    def _image_from_stream(self) -> Image:
        """
        Create a PIL Image object from the captured image stream.

        This method seeks to the beginning of the image stream, creates a PIL Image object from the stream data,
        and returns it.

        Returns:
            Image: The PIL Image object created from the captured image stream.

        Raises:
            None
        """
        self._stream.seek(0)
        return Img.open(self._stream)
