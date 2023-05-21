from ..reader import Reader
from .camera import Camera
from .ocr import OCR


class ImageReader(Reader):
    _camera: Camera
    _ocr: OCR

    def __init__(self, ocr: OCR, camera: Camera):
        self._camera = camera
        self._ocr = ocr

    def read(self) -> str:
        image = self._camera.capture()
        text = self._ocr.image_to_string(image)
        return text
