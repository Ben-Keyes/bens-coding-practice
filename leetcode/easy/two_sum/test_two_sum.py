import pytest
from two_sum import Solution


@pytest.fixture
def solution():
    return Solution()


class TestTwoSum:
    def test_cases(self, solution):
        assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert solution.twoSum([3, 2, 4], 6) == [1, 2]
        assert solution.twoSum([3, 3], 6) == [0, 1]
        assert solution.twoSum([1, 2, 3], 7) == []
