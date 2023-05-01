from directions import Directions


class Mapper:
    @classmethod
    def map(cls, letter: str) -> list[Directions]:
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
                return [Directions.NW, Directions.SW, Directions.E]
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
