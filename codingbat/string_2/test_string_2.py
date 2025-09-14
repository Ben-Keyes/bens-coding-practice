import pytest
from string_2 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestString2:
    def test_double_char(self, solution):
        assert solution.double_char("The") == "TThhee"
        assert solution.double_char("AAbb") == "AAAAbbbb"
        assert solution.double_char("Hi-There") == "HHii--TThheerree"
        assert solution.double_char("Word!") == "WWoorrdd!!"
        assert solution.double_char("") == ""
