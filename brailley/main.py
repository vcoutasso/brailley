from .directions import Directions
from .brailley import Brailley
from .solenoid import Solenoid
from PIL import Image
import pytesseract
import time

if __name__ == "__main__":
    image = Image.open('/home/usguri/1.png')

    text = pytesseract.image_to_string(image, config='')
    text = ''.join((ch.lower() if ch.isalpha() else '' for ch in text))

    brailley = Brailley({
        Directions.NW: Solenoid(13),
        Directions.W:  Solenoid(19),
        Directions.SW: Solenoid(26),
        Directions.NE: Solenoid(16),
        Directions.E:  Solenoid(20),
        Directions.SE: Solenoid(21),
    })

    for ch in text:
        print(f"Displaying {ch}")
        brailley.display(ch)
        time.sleep(1)

