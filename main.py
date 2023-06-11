from gpiozero.pins.pigpio import PiGPIOFactory
from brailley import Brailley
from gpiozero import Button
from time import sleep

if __name__ == "__main__":
    brailley = Brailley()
    button = Button(2, pin_factory=PiGPIOFactory())
    prev_state = True
    curr_state = False
    
    while(True):
        if button.is_pressed:
            if prev_state != curr_state:
                brailley.capture_and_display()
                curr_state = True
                sleep(0.15)
        else:
            curr_state = False
            sleep(0.15)
