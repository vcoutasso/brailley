from abc import ABC, abstractmethod
from io import BytesIO


class CameraIODevice(ABC):
    @abstractmethod
    def start_preview(self):
        pass

    @abstractmethod
    def capture(self, stream: BytesIO, **kwargs):
        pass
