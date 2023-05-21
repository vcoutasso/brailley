from abc import ABC, abstractmethod
from PIL import Image

class ImageFilter(ABC):
  @abstractmethod
  def apply(self, image: Image.Image) -> Image.Image:
    pass