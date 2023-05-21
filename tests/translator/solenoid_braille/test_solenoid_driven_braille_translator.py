from brailley.translator.solenoid_braille.solenoid_driven_braille_translator import (
    SolenoidDrivenBrailleTranslator,
)
from brailley.translator.solenoid_braille.directions import Directions
import pytest


class TestSolenoidDrivenBrailleTranslator:
    def test_init_should_fail_with_incomplete_directions(self):
        with pytest.raises(Exception):
            mapping = {Directions.SW: None}

            SolenoidDrivenBrailleTranslator(mapping)

    def test_init_should_fail_with_duplicated_directions(self):
        with pytest.raises(Exception):
            mapping = {Directions.SW: None, Directions.SW: None}

            SolenoidDrivenBrailleTranslator(mapping)

    def test_init_should_succeed_with_valid_mapping(self):
        mapping = {
            Directions.NW: 1,
            Directions.W: 2,
            Directions.SW: 3,
            Directions.NE: 4,
            Directions.E: 5,
            Directions.SE: 6,
        }

        SolenoidDrivenBrailleTranslator(mapping)

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

            SolenoidDrivenBrailleTranslator(mapping)
