import cv2
from PIL import Image
from image_filter import ImageFilter
import numpy as np

class NoiseRemovalFilter(ImageFilter):
    def apply(self, image: Image.Image) -> Image.Image:
        #convert image from pillow to opencv
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.medianBlur(image,5)
        #convert image from opencv to pillow
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return image