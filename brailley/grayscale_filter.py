import cv2
from PIL import Image
from image_filter import ImageFilter
import numpy as np

class GrayscaleFilter(ImageFilter):
    def apply(self, image: Image.Image) -> Image.Image:
        #convert image from pillow to opencv
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #convert image from opencv to pillow
        #image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return image