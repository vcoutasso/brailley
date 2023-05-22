from brailley.reader.image_reader.image_reader import ImageReader
from unittest import TestCase
from unittest.mock import Mock


class TestImageReader(TestCase):
    def setUp(self) -> None:
        self.mockOCR = Mock()
        self.mockCamera = Mock()
        self.mockFilter = Mock()
        self.sut = ImageReader(
            ocr=self.mockOCR, camera=self.mockCamera, filter=self.mockFilter
        )

    def test_read_shouldGetImageFromCamera(self):
        self.sut.read()

        self.mockCamera.capture.assert_called_once()

    def test_read_shouldApplyImagePreprocessing(self):
        self.sut.read()

        self.mockFilter.apply.assert_called_once()

    def test_read_shouldGetTextFromOCR(self):
        self.sut.read()

        self.mockOCR.image_to_string.assert_called_once()
