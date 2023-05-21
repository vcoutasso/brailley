from abc import ABC, abstractmethod
from PIL.Image import Image


class OCR(ABC):
    @abstractmethod
    def image_to_string(self, image: Image) -> str:
        pass
