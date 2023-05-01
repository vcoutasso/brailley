import gpiozero


class Solenoid:
    gpio = None

    def __init__(self, gpio):
        self.gpio = gpio
        self._output_device = gpiozero.OutputDevice(gpio)

    def __repr__(self):
        return f"Solenoid({self.gpio})"

    def __eq__(self, other):
        return isinstance(other, Solenoid) and self.gpio == other.gpio

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())

    def on(self):
        self._output_device.on()

    def off(self):
        self._output_device.off()
