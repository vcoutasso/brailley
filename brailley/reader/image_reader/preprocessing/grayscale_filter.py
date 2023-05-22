from .image_filter import ImageFilter
import numpy as np
import cv2


class GrayscaleFilter(ImageFilter):
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
