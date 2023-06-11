from .reader.image_reader.preprocessing import (
    GrayscaleFilter,
    BinaryFilter,
    MultipleFiltersDecorator,
)
from .translator.solenoid_braille import SolenoidDrivenBrailleTranslator
from .translator.solenoid_braille import Directions
from .translator.solenoid_braille import Solenoid
from .reader.image_reader import TesseractOCR
from .reader.image_reader import ImageReader
from .reader.image_reader import RPICamera
from .reader.image_reader import LEDFlash
import time

try:
    from picamera import PiCamera
except Exception:
    print("Could not import PiCamera, reading from camera will not work")


class Brailley:
    """
    Brailley class for capturing and displaying braille characters.

    This class provides a simple interface for capturing images using a Raspberry Pi camera,
    performing OCR on the captured image, and translating the recognized characters into braille
    using solenoids.

    Attributes:
        _translator (Translator): An instance of the translator used for braille translation.
        _reader (Reader): An instance of the reader used for image capture and OCR.

    Methods:
        capture_and_display(): Capture an image, perform OCR, and display the recognized braille characters.

    """

    def __init__(self):
        """
        Initialize the Brailley instance.

        This method sets up the necessary components for image capture, OCR, and braille translation.
        It creates instances of the necessary classes and configures them with appropriate parameters.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        mapping = {
            Directions.NW: Solenoid(13),
            Directions.W: Solenoid(19),
            Directions.SW: Solenoid(26),
            Directions.NE: Solenoid(16),
            Directions.E: Solenoid(20),
            Directions.SE: Solenoid(21),
        }

        ocr = TesseractOCR()
        flash = LEDFlash(17)
        try:
            camera_device = PiCamera(resolution=(1280, 720))
        except Exception:
            camera_device = None
        camera = RPICamera(flash=flash, camera_io_device=camera_device)
        filter = MultipleFiltersDecorator(filters=[GrayscaleFilter(), BinaryFilter()])

        self._translator = SolenoidDrivenBrailleTranslator(mapping)
        self._reader = ImageReader(ocr=ocr, camera=camera, filter=filter)

    def capture_and_display(self):
        """
        Capture an image, perform OCR, and display the recognized braille characters.

        This method captures an image using the Raspberry Pi camera, applies image preprocessing,
        performs OCR on the preprocessed image, translates the recognized characters into braille,
        and displays the resulting braille characters.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        input_string = self._reader.read()
        print(f"Read:\n{input_string}")
        clean_string = ' '.join(input_string.split()).lower()
        final_string = filter(lambda x: x == " " or x.isalpha(), clean_string)
        print(f"Will display:\n{''.join(final_string)}")
        for ch in final_string:
            self._translator.translate(ch)
            time.sleep(2)

        self._translator._reset()
