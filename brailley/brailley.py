from .translator.solenoid_braille.solenoid_driven_braille_translator import (
    SolenoidDrivenBrailleTranslator,
)
from .translator.solenoid_braille.directions import Directions
from .translator.solenoid_braille.solenoid import Solenoid
from .reader.image_reader.image_reader import ImageReader
from .reader.image_reader.tesseract_ocr import TesseractOCR
from .reader.image_reader.rpi_camera import RPICamera
from .reader.image_reader.led_flash import LEDFlash
from .reader.image_reader.preprocessing import (
    GrayscaleFilter,
    BinaryFilter,
    MultipleFiltersDecorator,
)
from .translator.translator import Translator
from .reader.reader import Reader
from picamera import PiCamera


class Brailley:
    _translator: Translator
    _reader: Reader

    def __init__(self):
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
        camera_device = PiCamera(resolution=(1280, 720))
        camera = RPICamera(flash=flash, camera_io_device=camera_device)
        filter = MultipleFiltersDecorator(filters=[GrayscaleFilter(), BinaryFilter()])

        self._translator = SolenoidDrivenBrailleTranslator(mapping)
        self._reader = ImageReader(ocr=ocr, camera=camera, filter=filter)

    def capture_and_display(self):
        input_string = self._reader.read()
        print(f"Now displaying:\n{input_string}")
        self._translator.translate(input_string)
