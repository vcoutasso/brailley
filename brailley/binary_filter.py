import cv2
from PIL import Image
from image_filter import ImageFilter
import numpy as np

class BinaryFilter(ImageFilter):
    def apply(self, image: Image.Image) -> Image.Image:
        #convert image from pillow to opencv
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #convert image from opencv to pillow
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
        return image