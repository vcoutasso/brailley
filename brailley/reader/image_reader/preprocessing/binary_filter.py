from .image_filter import ImageFilter
import numpy as np
import cv2


class BinaryFilter(ImageFilter):
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        grayscale_array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        _, binary_array = cv2.threshold(
            grayscale_array, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )
        return binary_array
