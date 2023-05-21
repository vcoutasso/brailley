from abc import ABC, abstractmethod
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LED


class Flash(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class LEDFlash(Flash):
    _led: LED

    def __init__(self, led_pin):
        self._led = LED(led_pin, pin_factory=PiGPIOFactory())

    def on(self):
        self._led.on()

    def off(self):
        self._led.off()
