import pytest
from warmup_1 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestWarmup1:
    def test_sleep_in(self, solution):
        assert solution.sleep_in(False, False) is True
        assert solution.sleep_in(True, False) is False
        assert solution.sleep_in(False, True) is True
        assert solution.sleep_in(True, True) is True

    def test_monkey_trouble(self, solution):
        assert solution.monkey_trouble(True, True) is True
        assert solution.monkey_trouble(False, False) is True
        assert solution.monkey_trouble(True, False) is False
        assert solution.monkey_trouble(False, True) is False

    def test_sum_double(self, solution):
        assert solution.sum_double(1, 2) == 3
        assert solution.sum_double(3, 2) == 5
        assert solution.sum_double(2, 2) == 8
        assert solution.sum_double(0, 0) == 0

    def test_diff21(self, solution):
        assert solution.diff21(19) == 2
        assert solution.diff21(10) == 11
        assert solution.diff21(21) == 0
        assert solution.diff21(25) == 8
        assert solution.diff21(-5) == 26

    def test_parrot_trouble(self, solution):
        assert solution.parrot_trouble(True, 6) is True
        assert solution.parrot_trouble(True, 7) is False
        assert solution.parrot_trouble(False, 6) is False
        assert solution.parrot_trouble(True, 21) is True
        assert solution.parrot_trouble(False, 21) is False

    def test_makes10(self, solution):
        assert solution.makes10(9, 10) is True
        assert solution.makes10(9, 9) is False
        assert solution.makes10(1, 9) is True
        assert solution.makes10(10, 1) is True
        assert solution.makes10(5, 5) is True

    def test_near_hundred(self, solution):
        assert solution.near_hundred(93) is True
        assert solution.near_hundred(90) is True
        assert solution.near_hundred(89) is False
        assert solution.near_hundred(110) is True
        assert solution.near_hundred(210) is True
        assert solution.near_hundred(211) is False

    def test_pos_neg(self, solution):
        assert solution.pos_neg(1, -1, False) is True
        assert solution.pos_neg(-1, 1, False) is True
        assert solution.pos_neg(-4, -5, True) is True
        assert solution.pos_neg(-4, -5, False) is False
        assert solution.pos_neg(1, 1, False) is False

    def test_not_string(self, solution):
        assert solution.not_string("candy") == "not candy"
        assert solution.not_string("x") == "not x"
        assert solution.not_string("not bad") == "not bad"
        assert solution.not_string("") == "not "
        assert solution.not_string("nothing") == "nothing"  # starts with "not"

    def test_missing_char(self, solution):
        assert solution.missing_char("kitten", 1) == "ktten"
        assert solution.missing_char("kitten", 0) == "itten"
        assert solution.missing_char("kitten", 4) == "kittn"
        assert solution.missing_char("a", 0) == ""

    def test_front_back(self, solution):
        assert solution.front_back("code") == "eodc"
        assert solution.front_back("a") == "a"
        assert solution.front_back("ab") == "ba"
        assert solution.front_back("abc") == "cba"

    def test_front3(self, solution):
        assert solution.front3("Java") == "JavJavJav"
        assert solution.front3("Chocolate") == "ChoChoCho"
        assert solution.front3("abc") == "abcabcabc"
        assert solution.front3("ab") == "ababab"
        assert solution.front3("a") == "aaa"
