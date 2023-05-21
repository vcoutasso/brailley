from brailley.translator.solenoid_braille.directions import Directions
from unittest import TestCase


class TestDirections(TestCase):
    def test_directions_length(self):
        self.assertEqual(len(Directions), 6)

    def test_nw(self):
        self.assertEqual(Directions.NW.value, 0)

    def test_w(self):
        self.assertEqual(Directions.W.value, 1)

    def test_sw(self):
        self.assertEqual(Directions.SW.value, 2)

    def test_ne(self):
        self.assertEqual(Directions.NE.value, 3)

    def test_e(self):
        self.assertEqual(Directions.E.value, 4)

    def test_se(self):
        self.assertEqual(Directions.SE.value, 5)
