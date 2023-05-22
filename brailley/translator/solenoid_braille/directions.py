from enum import Enum


class Directions(Enum):
    """
    Enumeration representing directions.

    This enumeration defines different directions as named constants.

    Attributes:
        NW (int): North-west direction.
        W (int): West direction.
        SW (int): South-west direction.
        NE (int): North-east direction.
        E (int): East direction.
        SE (int): South-east direction.
    """

    NW = 0
    W = 1
    SW = 2
    NE = 3
    E = 4
    SE = 5
