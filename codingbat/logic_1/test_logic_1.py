import pytest
from logic_1 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestLogic1:
    def test_cigar_party(self, solution):
        assert solution.cigar_party(30, False) is False
        assert solution.cigar_party(50, False) is True
        assert solution.cigar_party(70, False) is False
        assert solution.cigar_party(70, True) is True
        assert solution.cigar_party(40, True) is True

    def test_date_fashion(self, solution):
        assert solution.date_fashion(5, 10) == 2
        assert solution.date_fashion(2, 9) == 0
        assert solution.date_fashion(5, 5) == 1
        assert solution.date_fashion(9, 2) == 0
        assert solution.date_fashion(8, 8) == 2

    def test_squirrel_play(self, solution):
        assert solution.squirrel_play(70, False) is True
        assert solution.squirrel_play(95, False) is False
        assert solution.squirrel_play(95, True) is True
        assert solution.squirrel_play(59, True) is False
        assert solution.squirrel_play(100, True) is True

    def test_caught_speeding(self, solution):
        assert solution.caught_speeding(60, False) == 0
        assert solution.caught_speeding(65, True) == 0
        assert solution.caught_speeding(75, False) == 1
        assert solution.caught_speeding(85, True) == 1
        assert solution.caught_speeding(90, False) == 2
