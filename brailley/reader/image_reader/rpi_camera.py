from io import BytesIO
from PIL import Image as Img
from PIL.Image import Image
from time import sleep
from .flash import Flash
from .camera_io_device import CameraIODevice
from .camera import Camera


class RPICamera(Camera):
    _flash: Flash
    _camera: CameraIODevice
    _stream: BytesIO

    def __init__(self, flash: Flash, camera_io_device: CameraIODevice, warmup: int = 2):
        self._flash = flash
        self._camera = camera_io_device
        self._stream = BytesIO()
        self._camera.start_preview()
        # camera warm-up
        sleep(warmup)

    def capture(self) -> Image:
        self._flash.on()
        self._camera.capture(self._stream, format="jpeg")
        self._flash.off()

        return self._image_from_stream()

    def _image_from_stream(self) -> Image:
        self._stream.seek(0)
        return Img.open(self._stream)
