from directions import Directions
from brailley import Brailley
import pytest


class TestBrailley:
    def test_init_should_fail_with_incomplete_directions(self):
        with pytest.raises(Exception):
            mapping = {Directions.SW: None}

            Brailley(mapping)

    def test_init_should_fail_with_duplicated_directions(self):
        with pytest.raises(Exception):
            mapping = {Directions.SW: None, Directions.SW: None}

            Brailley(mapping)

    def test_init_should_succeed_with_valid_mapping(self):
        mapping = {
            Directions.NW: 1,
            Directions.W: 2,
            Directions.SW: 3,
            Directions.NE: 4,
            Directions.E: 5,
            Directions.SE: 6,
        }

        Brailley(mapping)

    def test_init_should_fail_with_duplicated_solenoids(self):
        with pytest.raises(Exception):
            mapping = {
                Directions.NW: 1,
                Directions.W: 1,
                Directions.SW: 3,
                Directions.NE: 4,
                Directions.E: 5,
                Directions.SE: 6,
            }

            Brailley(mapping)
