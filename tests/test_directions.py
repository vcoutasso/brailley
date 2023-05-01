from directions import Directions


class TestDirections:
    def test_directions_length(self):
        assert len(Directions) == 6

    def test_nw(self):
        assert Directions.NW.value == 0

    def test_w(self):
        assert Directions.W.value == 1

    def test_sw(self):
        assert Directions.SW.value == 2

    def test_ne(self):
        assert Directions.NE.value == 3

    def test_e(self):
        assert Directions.E.value == 4

    def test_se(self):
        assert Directions.SE.value == 5
