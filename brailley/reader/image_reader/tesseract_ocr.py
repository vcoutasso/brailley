from PIL.Image import Image
from .ocr import OCR
import pytesseract


class TesseractOCR(OCR):
    """
    Concrete class representing an OCR (Optical Character Recognition) system using Tesseract.

    This class extends the OCR class and implements the 'image_to_string'
    method to extract text from an image using Tesseract.

    Attributes:
        None
    """

    def image_to_string(self, image: Image) -> str:
        """
        Extract text from the given image using Tesseract OCR.

        This method uses the pytesseract library to perform OCR on the given image and extract the text.

        Args:
            image (Image): The image to perform OCR on.

        Returns:
            str: The extracted text from the image.

        Raises:
            None
        """
        return pytesseract.image_to_string(image, config="")
