import pytest
from list_1 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestList1:
    def test_first_last6(self, solution):
        assert solution.first_last6([1, 2, 6]) is True
        assert solution.first_last6([6, 1, 2, 3]) is True
        assert solution.first_last6([13, 6, 1, 2, 3]) is False
        assert solution.first_last6([6]) is True
        assert solution.first_last6([1, 2, 3, 4, 5]) is False

    def test_make_pi(self, solution):
        assert solution.make_pi() == [3, 1, 4]
        assert len(solution.make_pi()) == 3
        assert solution.make_pi()[0] == 3
        assert solution.make_pi()[1] == 1
        assert solution.make_pi()[2] == 4

    def test_common_end(self, solution):
        assert solution.common_end([1, 2, 3], [7, 3]) is True
        assert solution.common_end([1, 2, 3], [1, 3]) is True
        assert solution.common_end([1, 2, 3], [4, 5, 6]) is False
        assert solution.common_end([5], [5, 6, 7]) is True
        assert solution.common_end([8, 2, 3], [1, 2, 3]) is True

    def test_sum3(self, solution):
        assert solution.sum3([1, 2, 3]) == 6
        assert solution.sum3([5, 11, 2]) == 18
        assert solution.sum3([7, 0, 0]) == 7
        assert solution.sum3([9, 9, 9]) == 27
        assert solution.sum3([-1, -2, -3]) == -6

    def test_rotate_left3(self, solution):
        assert solution.rotate_left3([1, 2, 3]) == [2, 3, 1]
        assert solution.rotate_left3([5, 11, 9]) == [11, 9, 5]
        assert solution.rotate_left3([7, 0, 0]) == [0, 0, 7]
        assert solution.rotate_left3([1, 2, 1]) == [2, 1, 1]
        assert solution.rotate_left3([0, 1, 2]) == [1, 2, 0]
