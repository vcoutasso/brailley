from brailley.translator.solenoid_braille.directions import Directions
from brailley.translator.solenoid_braille.braille_mapper import BrailleMapper
import collections
from unittest import TestCase


class TestBrailleMapper(TestCase):
    def test_unsupported_mapping(self):
        self.assertEqual(BrailleMapper.map("this is an unsupported string"), [])

    def test_mappings(self):
        for key in self._braille_lookup.keys():
            self.assertEqual(
                collections.Counter(BrailleMapper.map(key)),
                collections.Counter(self._lookup_to_directions(key)),
                msg=f"Representation differs for {key}",
            )

    def _lookup_to_directions(self, key):
        directions = []
        indices = []

        for i, v in enumerate(self._braille_lookup[key]):
            if v:
                indices.append(i)

        for idx in indices:
            directions.append(Directions(idx))

        return directions

    _braille_lookup = {
        "a": (1, 0, 0, 0, 0, 0),
        "b": (1, 1, 0, 0, 0, 0),
        "c": (1, 0, 0, 1, 0, 0),
        "d": (1, 0, 0, 1, 1, 0),
        "e": (1, 0, 0, 0, 1, 0),
        "f": (1, 1, 0, 1, 0, 0),
        "g": (1, 1, 0, 1, 1, 0),
        "h": (1, 1, 0, 0, 1, 0),
        "i": (0, 1, 0, 1, 0, 0),
        "j": (0, 1, 0, 1, 1, 0),
        "k": (1, 0, 1, 0, 0, 0),
        "l": (1, 1, 1, 0, 0, 0),
        "m": (1, 0, 1, 1, 0, 0),
        "n": (1, 0, 1, 1, 1, 0),
        "o": (1, 0, 1, 0, 1, 0),
        "p": (1, 1, 1, 1, 0, 0),
        "q": (1, 1, 1, 1, 1, 0),
        "r": (1, 1, 1, 0, 1, 0),
        "s": (0, 1, 1, 1, 0, 0),
        "t": (0, 1, 1, 1, 1, 0),
        "u": (1, 0, 1, 0, 0, 1),
        "v": (1, 1, 1, 0, 0, 1),
        "w": (0, 1, 0, 1, 1, 1),
        "x": (1, 0, 1, 1, 0, 1),
        "y": (1, 0, 1, 1, 1, 1),
        "z": (1, 0, 1, 0, 1, 1),
        "ç": (1, 1, 1, 1, 0, 1),
    }
