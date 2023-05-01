from directions import Directions
from solenoid import Solenoid
from mapper import Mapper


class Brailley:
    def __init__(self, mapping):
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


if __name__ == "__main__":
    dict = {
        Directions.NW: Solenoid(1),
        Directions.NE: Solenoid(2),
        Directions.W: Solenoid(3),
        Directions.E: Solenoid(4),
        Directions.SW: Solenoid(5),
        Directions.SE: Solenoid(6),
    }

    brailley = Brailley(dict)

    brailley.display("a")
