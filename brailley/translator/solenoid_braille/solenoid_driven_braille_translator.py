from .directions import Directions
from .solenoid import Solenoid
from .braille_mapper import BrailleMapper
from ..translator import Translator


class SolenoidDrivenBrailleTranslator(Translator):
    def __init__(self, mapping: dict[Directions, Solenoid]):
        if len(mapping) != len(Directions):
            raise Exception("Mapping should contemplate all directions")
        if len(set(mapping.values())) != len(Directions):
            raise Exception("Mapping should not contain duplicated solenoids")

        self.mapping = mapping

    def translate(self, letter: str) -> None:
        self._reset()

        for pos in BrailleMapper.map(letter):
            self.mapping[pos].on()

    def _reset(self):
        for solenoid in self.mapping.values():
            solenoid.off()
