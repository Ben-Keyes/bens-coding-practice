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

    def test_sorta_sum(self, solution):
        assert solution.sorta_sum(3, 4) == 7
        assert solution.sorta_sum(9, 4) == 20
        assert solution.sorta_sum(10, 10) == 20
        assert solution.sorta_sum(6, 4) == 20
        assert solution.sorta_sum(20, 0) == 20

    def test_alarm_clock(self, solution):
        assert solution.alarm_clock(1, False) == "7:00"
        assert solution.alarm_clock(5, False) == "7:00"
        assert solution.alarm_clock(0, False) == "10:00"
        assert solution.alarm_clock(6, True) == "off"
        assert solution.alarm_clock(3, True) == "10:00"

    def test_love6(self, solution):
        assert solution.love6(6, 4) is True
        assert solution.love6(4, 5) is False
        assert solution.love6(1, 5) is True
        assert solution.love6(12, 6) is True
        assert solution.love6(7, 1) is True

    def test_in1to10(self, solution):
        assert solution.in1to10(5, False) is True
        assert solution.in1to10(11, False) is False
        assert solution.in1to10(1, False) is True
        assert solution.in1to10(0, True) is True
        assert solution.in1to10(10, True) is True

    def test_near_ten(self, solution):
        assert solution.near_ten(12) is True
        assert solution.near_ten(17) is False
        assert solution.near_ten(19) is True
        assert solution.near_ten(20) is True
        assert solution.near_ten(3) is False
