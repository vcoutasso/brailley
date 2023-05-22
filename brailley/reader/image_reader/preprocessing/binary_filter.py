import cv2
from PIL import Image
from image_filter import ImageFilter
import numpy as np


class BinaryFilter(ImageFilter):
    def apply(self, image: Image.Image) -> Image.Image:
        image_array = self.pillow_to_npy(image)
        binary_array = self.apply_npy(image_array)
        return self.npy_to_pillow(binary_array)

    def apply_npy(self, array: np.ndarray) -> np.ndarray:
        grayscale_array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        _, binary_array = cv2.threshold(
            grayscale_array, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )
        return binary_array
