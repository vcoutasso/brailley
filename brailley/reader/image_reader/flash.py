from abc import ABC, abstractmethod


class Flash(ABC):
    """
    Abstract base class representing a flash.

    This class defines the common interface for flashes. Subclasses must implement the 'on' and 'off' methods.

    Attributes:
        None
    """

    @abstractmethod
    def on(self):
        """
        Turn on the flash.

        This method should be implemented by subclasses to turn on the flash.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass

    @abstractmethod
    def off(self):
        """
        Turn off the flash.

        This method should be implemented by subclasses to turn off the flash.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
