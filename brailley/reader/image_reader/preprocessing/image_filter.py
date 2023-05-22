from abc import ABC, abstractmethod
from PIL import Image as Img
from PIL.Image import Image
import numpy as np
import cv2


class ImageFilter(ABC):
    @abstractmethod
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        pass

    def apply(self, image: Image) -> Image:
        image_array = self.pillow_to_npy(image)
        filtered_array = self.apply_filter(image_array)
        return self.npy_to_pillow(filtered_array)

    def pillow_to_npy(self, image: Image) -> np.ndarray:
        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    def npy_to_pillow(self, array: np.ndarray) -> Image:
        return Img.fromarray(cv2.cvtColor(array, cv2.COLOR_BGR2RGB))
