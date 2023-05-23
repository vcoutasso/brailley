from brailley import Brailley
from gpiozero import Button
from signal import pause

if __name__ == "__main__":
    brailley = Brailley()
    button = Button(2)

    button.when_pressed = brailley.capture_and_display

    pause()
