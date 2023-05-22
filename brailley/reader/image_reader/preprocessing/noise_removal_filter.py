from .image_filter import ImageFilter
import numpy as np
import cv2


class NoiseRemovalFilter(ImageFilter):
    def apply_filter(self, array: np.ndarray) -> np.ndarray:
        return cv2.medianBlur(array, 5)
