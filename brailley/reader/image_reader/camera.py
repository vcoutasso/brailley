from io import BytesIO
from picamera import PiCamera
from PIL import Image as Img
from PIL.Image import Image
from time import sleep
from .flash import Flash, LEDFlash


class Camera:
    _flash: LEDFlash
    _camera: PiCamera
    _stream: BytesIO

    def __init__(self, flash: Flash):
        self._flash = flash
        self._camera = PiCamera(
            resolution=(1280, 720),
        )
        self._stream = BytesIO()
        self._camera.start_preview()
        # camera warm-up
        sleep(2)

    def capture(self) -> Image:
        self._flash.on()
        self._camera.capture(self._stream, format="jpeg")
        self._flash.off()

        return self._image_from_stream()

    def _image_from_stream(self) -> Image:
        self._stream.seek(0)
        return Img.open(self._stream)
