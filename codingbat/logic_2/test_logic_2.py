import pytest
from logic_2 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestLogic2:
    def test_make_bricks(self, solution):
        assert solution.make_bricks(3, 1, 8) is True
        assert solution.make_bricks(3, 1, 9) is False
        assert solution.make_bricks(3, 2, 10) is True
        assert solution.make_bricks(0, 3, 14) is False
        assert solution.make_bricks(7, 1, 12) is True

    def test_lone_sum(self, solution):
        assert solution.lone_sum(1, 2, 3) == 6
        assert solution.lone_sum(3, 2, 3) == 2
        assert solution.lone_sum(3, 3, 3) == 0
        assert solution.lone_sum(5, 5, 7) == 7
        assert solution.lone_sum(10, 9, 10) == 9

    def test_lucky_sum(self, solution):
        assert solution.lucky_sum(1, 2, 3) == 6
        assert solution.lucky_sum(1, 2, 13) == 3
        assert solution.lucky_sum(1, 13, 3) == 1
        assert solution.lucky_sum(13, 2, 3) == 0
        assert solution.lucky_sum(13, 13, 13) == 0

    def test_no_teen_sum(self, solution):
        assert solution.no_teen_sum(1, 2, 3) == 6
        assert solution.no_teen_sum(2, 13, 1) == 3
        assert solution.no_teen_sum(2, 1, 14) == 3
        assert solution.no_teen_sum(2, 15, 14) == 17
        assert solution.no_teen_sum(16, 17, 18) == 16

    def test_round_sum(self, solution):
        assert solution.round_sum(16, 17, 18) == 60
        assert solution.round_sum(12, 13, 14) == 30
        assert solution.round_sum(6, 4, 4) == 10
        assert solution.round_sum(15, 25, 35) == 90
        assert solution.round_sum(11, 21, 29) == 60

    def test_close_far(self, solution):
        assert solution.close_far(1, 2, 10) is True
        assert solution.close_far(1, 2, 3) is False
        assert solution.close_far(4, 5, 9) is True
        assert solution.close_far(10, 9, 8) is False
        assert solution.close_far(5, 6, 4) is False
