from directions import Directions
from solenoid import Solenoid


class Brailley:
    def __init__(self, mapping):
        if len(mapping) != len(Directions):
            raise Exception("Mapping should contemplate all directions")
        if len(set(mapping.values())) != len(Directions):
            raise Exception("Mapping should not contain duplicated solenoids")

        self.mapping = mapping

    def display(self, letter: str):
        self.reset()

        for pos in self._map(letter):
            self.mapping[pos].on()

    def reset(self):
        for solenoid in self.mapping.values():
            solenoid.off()

    def _map(self, letter: str):
        match letter:
            case "a":
                return [Directions.NW]
            case "b":
                return [Directions.NW, Directions.W]
            case "c":
                return [Directions.NW, Directions.NE]
            case "d":
                return [Directions.NW, Directions.NE, Directions.E]
            case "e":
                return [Directions.NW, Directions.E]
            case "f":
                return [Directions.NW, Directions.W, Directions.NE]
            case "g":
                return [Directions.NW, Directions.W, Directions.NE, Directions.E]
            case "h":
                return [Directions.NW, Directions.W, Directions.E]
            case "i":
                return [Directions.W, Directions.NE]
            case "j":
                return [Directions.W, Directions.NE, Directions.E]
            case "k":
                return [Directions.NW, Directions.SW]
            case "l":
                return [Directions.NW, Directions.W, Directions.SW]
            case "m":
                return [Directions.NW, Directions.SW, Directions.NE]
            case "n":
                return [Directions.NW, Directions.SW, Directions.NE, Directions.E]
            case "o":
                return [Directions.NW, Directions.SW, Directions.SE]
            case "p":
                return [Directions.NW, Directions.W, Directions.SW, Directions.NE]
            case "q":
                return [
                    Directions.NW,
                    Directions.W,
                    Directions.SW,
                    Directions.NE,
                    Directions.E,
                ]
            case "r":
                return [Directions.NW, Directions.W, Directions.SW, Directions.E]
            case "s":
                return [Directions.W, Directions.SW, Directions.NE]
            case "t":
                return [Directions.W, Directions.SW, Directions.NE, Directions.E]
            case "u":
                return [Directions.NW, Directions.SW, Directions.SE]
            case "v":
                return [Directions.NW, Directions.W, Directions.SW, Directions.SE]
            case "w":
                return [Directions.W, Directions.NE, Directions.E, Directions.SE]
            case "x":
                return [Directions.NW, Directions.SW, Directions.NE, Directions.SE]
            case "y":
                return [
                    Directions.NW,
                    Directions.SW,
                    Directions.NE,
                    Directions.E,
                    Directions.SE,
                ]
            case "z":
                return [Directions.NW, Directions.SW, Directions.E, Directions.SE]
            case "ç":
                return [
                    Directions.NW,
                    Directions.W,
                    Directions.SW,
                    Directions.NE,
                    Directions.SE,
                ]
            case _:
                return []


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
