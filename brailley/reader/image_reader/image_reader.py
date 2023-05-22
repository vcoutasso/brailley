from ..reader import Reader
from .camera import Camera
from .preprocessing import ImageFilter
from .ocr import OCR


class ImageReader(Reader):
    """
    Concrete class representing an image reader.

    This class extends the Reader class and implements the 'read' method to read text from an image.

    Attributes:
        _camera (Camera): The camera used for capturing images.
        _ocr (OCR): The OCR (Optical Character Recognition) system used for text extraction.
        _filter (ImageFilter): The image filter used for preprocessing.

    """

    _camera: Camera
    _ocr: OCR
    _filter: ImageFilter

    def __init__(self, ocr: OCR, camera: Camera, filter: ImageFilter):
        """
        Initialize the ImageReader with the specified OCR, camera, and image filter.

        Args:
            ocr (OCR): The OCR (Optical Character Recognition) system used for text extraction.
            camera (Camera): The camera used for capturing images.
            filter (ImageFilter): The image filter used for preprocessing.

        Returns:
            None

        Raises:
            None
        """
        self._camera = camera
        self._ocr = ocr
        self._filter = filter

    def read(self) -> str:
        """
        Read text from an image.

        This method captures an image using the camera, applies the image filter for preprocessing, performs OCR to
        extract text from the filtered image, and returns the extracted text.

        Returns:
            str: The extracted text from the image.

        Raises:
            None
        """
        image = self._camera.capture()
        filtered_image = self._filter.apply(image)
        text = self._ocr.image_to_string(filtered_image)
        return text
