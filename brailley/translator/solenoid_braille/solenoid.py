import gpiozero


class Solenoid:
    """
    Class representing a solenoid.

    This class provides functionality to control a solenoid connected to a GPIO pin.

    Attributes:
        gpio (int): The GPIO pin number used to control the solenoid.
        _output_device (gpiozero.OutputDevice): The output device used to control the GPIO pin.

    Methods:
        __init__(gpio: int): Initialize the Solenoid instance with the specified GPIO pin number.
        __repr__(): Return a string representation of the Solenoid instance.
        __eq__(other): Compare the Solenoid instance with another object for equality.
        __ne__(other): Compare the Solenoid instance with another object for inequality.
        __hash__(): Return the hash value of the Solenoid instance.
        on(): Turn on the solenoid.
        off(): Turn off the solenoid.
    """

    def __init__(self, gpio: int):
        """
        Initialize the Solenoid instance with the specified GPIO pin number.

        Args:
            gpio (int): The GPIO pin number used to control the solenoid.

        Returns:
            None

        Raises:
            None
        """
        self.gpio = gpio
        self._output_device = gpiozero.OutputDevice(
            gpio, pin_factory=gpiozero.pins.pigpio.PiGPIOFactory()
        )

    def __repr__(self):
        """
        Return a string representation of the Solenoid instance.

        Returns:
            str: A string representation of the Solenoid instance.

        Raises:
            None
        """
        return f"Solenoid({self.gpio})"

    def __eq__(self, other):
        """
        Compare the Solenoid instance with another object for equality.

        Args:
            other: The object to compare with the Solenoid instance.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Raises:
            None
        """
        return isinstance(other, Solenoid) and self.gpio == other.gpio

    def __ne__(self, other):
        """
        Compare the Solenoid instance with another object for inequality.

        Args:
            other: The object to compare with the Solenoid instance.

        Returns:
            bool: True if the objects are not equal, False otherwise.

        Raises:
            None
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        Return the hash value of the Solenoid instance.

        Returns:
            int: The hash value of the Solenoid instance.

        Raises:
            None
        """
        return hash(self.__repr__())

    def on(self):
        """
        Turn on the solenoid.

        This method activates the solenoid by turning on the associated GPIO pin.

        Returns:
            None

        Raises:
            None
        """
        self._output_device.on()

    def off(self):
        """
        Turn off the solenoid.

        This method deactivates the solenoid by turning off the associated GPIO pin.

        Returns:
            None

        Raises:
            None
        """
        self._output_device.off()
