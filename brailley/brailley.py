from .directions import Directions
from .solenoid import Solenoid
from .mapper import Mapper


class Brailley:
    def __init__(self, mapping: dict[Directions, Solenoid]):
        if len(mapping) != len(Directions):
            raise Exception("Mapping should contemplate all directions")
        if len(set(mapping.values())) != len(Directions):
            raise Exception("Mapping should not contain duplicated solenoids")

        self.mapping = mapping

    def display(self, letter: str):
        self.reset()

        for pos in Mapper.map(letter):
            self.mapping[pos].on()

    def reset(self):
        for solenoid in self.mapping.values():
            solenoid.off()
