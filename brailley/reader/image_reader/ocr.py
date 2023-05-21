from PIL.Image import Image
import pytesseract


class OCR:
    def image_to_string(self, image: Image) -> str:
        return pytesseract.image_to_string(image, config="")
