from .directions import Directions
from .solenoid import Solenoid
from .braille_mapper import BrailleMapper
from ..translator import Translator


class SolenoidDrivenBrailleTranslator(Translator):
    """
    Class representing a Solenoid-driven Braille translator.

    This class translates letters into Braille by controlling solenoids based on a mapping of directions.

    Attributes:
        mapping (dict[Directions, Solenoid]): A dictionary mapping Directions to Solenoid objects.

    Methods:
        translate(letter: str) -> None: Translate a letter into Braille by controlling the corresponding solenoids.
        _reset() -> None: Reset all solenoids to the off state.

    Raises:
        Exception: Raised when the mapping does not contemplate all directions or contains duplicated solenoids.
    """

    def __init__(self, mapping: dict[Directions, Solenoid]):
        """
        Initialize the SolenoidDrivenBrailleTranslator with a mapping of directions to solenoids.

        Args:
            mapping (dict[Directions, Solenoid]): A dictionary mapping Directions to Solenoid objects.

        Returns:
            None
        """
        if len(mapping) != len(Directions):
            raise Exception("Mapping should contemplate all directions")
        if len(set(mapping.values())) != len(Directions):
            raise Exception("Mapping should not contain duplicated solenoids")

        self.mapping = mapping

    def translate(self, letter: str) -> None:
        """
        Translate a letter into Braille by controlling the corresponding solenoids.

        This method takes a letter as input and controls the solenoids based on the Braille mapping of the letter.
        It turns on the solenoids corresponding to the mapped directions.

        Args:
            letter (str): The letter to translate into Braille.

        Returns:
            None

        Raises:
            None
        """
        self._reset()

        for pos in BrailleMapper.map(letter):
            self.mapping[pos].on()

    def _reset(self):
        """
        Reset all solenoids to the off state.

        This method turns off all solenoids in the mapping.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        for solenoid in self.mapping.values():
            solenoid.off()
