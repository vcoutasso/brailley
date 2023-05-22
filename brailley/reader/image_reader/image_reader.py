from ..reader import Reader
from .camera import Camera
from .preprocessing import ImageFilter
from .ocr import OCR


class ImageReader(Reader):
    _camera: Camera
    _ocr: OCR
    _filter: ImageFilter

    def __init__(self, ocr: OCR, camera: Camera, filter: ImageFilter):
        self._camera = camera
        self._ocr = ocr
        self._filter = filter

    def read(self) -> str:
        image = self._camera.capture()
        filtered_image = self._filter.apply(image)
        text = self._ocr.image_to_string(filtered_image)
        return text
