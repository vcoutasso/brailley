from abc import ABC, abstractmethod
from typing import Any


class Translator(ABC):
    """
    Abstract base class for translators.

    This class defines the interface for translators. Subclasses must implement the `translate` method.

    Methods:
        translate(input: Any) -> Any: Translate the input into the desired output.

    """

    @abstractmethod
    def translate(self, input: Any) -> Any:
        """
        Abstract method to be implemented by subclasses.

        This method takes an input and performs the translation into the desired output.

        Args:
            input (Any): The input to be translated.

        Returns:
            Any: The translated output.

        Raises:
            None
        """
        pass
