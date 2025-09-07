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
