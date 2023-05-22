from abc import ABC, abstractmethod


class Reader(ABC):
    """
    Abstract base class representing a reader.

    This class defines the common interface for readers. Subclasses must implement the 'read' method.

    Attributes:
        None
    """

    @abstractmethod
    def read(self) -> str:
        """
        Read and retrieve data from a source.

        This method should be implemented by subclasses to read and retrieve data from a specific source.

        Returns:
            str: The data read from the source.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.
        """
        pass
