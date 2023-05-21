from abc import ABC, abstractmethod
from PIL.Image import Image


class Camera(ABC):
    @abstractmethod
    def capture(self) -> Image:
        pass
