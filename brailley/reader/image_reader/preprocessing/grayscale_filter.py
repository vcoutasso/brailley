import cv2
from PIL import Image
from image_filter import ImageFilter
import numpy as np


class GrayscaleFilter(ImageFilter):
    def apply(self, image: Image.Image) -> Image.Image:
        image_array = self.pillow_to_npy(image)
        grayscale_array = self.apply_npy(image_array)
        return self.npy_to_pillow(grayscale_array)

    def apply_npy(self, array: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
