from .directions import Directions


class BrailleMapper:
    """
    Class representing a Braille mapper.

    This class provides a mapping of letters to Braille directions.

    Attributes:
        None

    Methods:
        map(letter: str) -> list[Directions]: Map a letter to a list of Braille directions.
    """

    @classmethod
    def map(cls, letter: str) -> list[Directions]:
        """
        Map a letter to a list of Braille directions.

        This method takes a letter as input and returns a list of Braille directions corresponding to that letter.
        If the letter is not recognized, an empty list is returned.

        Args:
            letter (str): The letter to map to Braille directions.

        Returns:
            list[Directions]: A list of Braille directions.

        Raises:
            None
        """
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
