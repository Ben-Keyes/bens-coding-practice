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

    def test_reverse3(self, solution):
        assert solution.reverse3([1, 2, 3]) == [3, 2, 1]
        assert solution.reverse3([5, 11, 9]) == [9, 11, 5]
        assert solution.reverse3([7, 0, 0]) == [0, 0, 7]
        assert solution.reverse3([2, 1, 2]) == [2, 1, 2]
        assert solution.reverse3([1, 2, 1]) == [1, 2, 1]

    def test_max_end3(self, solution):
        assert solution.max_end3([1, 2, 3]) == [3, 3, 3]
        assert solution.max_end3([11, 5, 9]) == [11, 11, 11]
        assert solution.max_end3([2, 11, 3]) == [3, 3, 3]
        assert solution.max_end3([20, 30, 10]) == [20, 20, 20]
        assert solution.max_end3([7, 8, 6]) == [7, 7, 7]

    def test_sum2(self, solution):
        assert solution.sum2([1, 2, 3]) == 3
        assert solution.sum2([5]) == 5
        assert solution.sum2([]) == 0
        assert solution.sum2([1, 1, 1, 1]) == 2
        assert solution.sum2([10, -5]) == 5

    def test_middle_way(self, solution):
        assert solution.middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
        assert solution.middle_way([7, 8, 9], [1, 3, 5]) == [8, 3]
        assert solution.middle_way([0, 0, 0], [1, 2, 3]) == [0, 2]
        assert solution.middle_way([-1, -2, -3], [10, 20, 30]) == [-2, 20]
        assert solution.middle_way([5, 5, 5], [5, 5, 5]) == [5, 5]

    def test_make_ends(self, solution):
        assert solution.make_ends([1, 2, 3]) == [1, 3]
        assert solution.make_ends([5, 10, 20, 30]) == [5, 30]
        assert solution.make_ends([7]) == [7, 7]
        assert solution.make_ends([0, 1, 0]) == [0, 0]
        assert solution.make_ends([-1, 0, 1]) == [-1, 1]

    def test_has23(self, solution):
        assert solution.has23([2, 5]) is True
        assert solution.has23([4, 3]) is True
        assert solution.has23([4, 5]) is False
        assert solution.has23([2, 3]) is True
        assert solution.has23([0, 0]) is False
