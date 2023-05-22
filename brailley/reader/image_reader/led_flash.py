from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED
from .flash import Flash


class LEDFlash(Flash):
    """
    Concrete class representing an LED flash.

    This class extends the abstract class Flash and implements the 'on' and 'off' methods to control an LED flash.

    Attributes:
        _led (LED): The LED instance representing the flash.
    """

    _led: LED

    def __init__(self, led_pin):
        """
        Initialize the LEDFlash with the specified LED pin.

        Args:
            led_pin: The pin number of the LED.

        Returns:
            None

        Raises:
            None
        """
        self._led = LED(led_pin, pin_factory=PiGPIOFactory())

    def on(self):
        """
        Turn on the LED flash.

        This method turns on the LED flash.

        Returns:
            None

        Raises:
            None
        """
        self._led.on()

    def off(self):
        """
        Turn off the LED flash.

        This method turns off the LED flash.

        Returns:
            None

        Raises:
            None
        """
        self._led.off()
