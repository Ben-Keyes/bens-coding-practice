import pytest
from warmup_2 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestWarmup2:
    def test_string_times(self, solution):
        assert solution.string_times("Hi", 2) == "HiHi"
        assert solution.string_times("Hi", 3) == "HiHiHi"
        assert solution.string_times("Hi", 1) == "Hi"
        assert solution.string_times("Hi", 0) == ""
        assert solution.string_times("", 4) == ""

    def test_front_times(self, solution):
        assert solution.front_times("Chocolate", 2) == "ChoCho"
        assert solution.front_times("Chocolate", 3) == "ChoChoCho"
        assert solution.front_times("Ab", 4) == "AbAbAbAb"
        assert solution.front_times("", 3) == ""
        assert solution.front_times("X", 5) == "XXXXX"

    def test_string_bits(self, solution):
        assert solution.string_bits("Hello") == "Hlo"
        assert solution.string_bits("Hi") == "H"
        assert solution.string_bits("Heeololeo") == "Hello"
        assert solution.string_bits("") == ""
        assert solution.string_bits("H") == "H"

    def test_string_splosion(self, solution):
        assert solution.string_splosion("Code") == "CCoCodCode"
        assert solution.string_splosion("abc") == "aababc"
        assert solution.string_splosion("ab") == "aab"
        assert solution.string_splosion("x") == "x"
        assert solution.string_splosion("") == ""

    def test_last2(self, solution):
        assert solution.last2("hixxxhi") == 1
        assert solution.last2("axxxaaxx") == 2
        assert solution.last2("abcdef") == 0
        assert solution.last2("hi") == 0
        assert solution.last2("h") == 0

    def test_array_count9(self, solution):
        assert solution.array_count9([1, 9, 9, 3, 9]) == 3
        assert solution.array_count9([1, 2, 3, 4, 5]) == 0
        assert solution.array_count9([9, 9, 9, 9]) == 4
        assert solution.array_count9([]) == 0
        assert solution.array_count9([9]) == 1

    def test_array_front9(self, solution):
        assert solution.array_front9([1, 2, 9, 3, 4]) is True
        assert solution.array_front9([1, 2, 3, 4, 9]) is False
        assert solution.array_front9([9, 1, 2, 3]) is True
        assert solution.array_front9([1, 2, 3]) is False
        assert solution.array_front9([]) is False

    def test_array123(self, solution):
        assert solution.array123([1, 2, 3]) is True
        assert solution.array123([0, 1, 2, 3, 4]) is True
        assert solution.array123([1, 2]) is False
        assert solution.array123([1, 2, 4, 3]) is False
        assert solution.array123([]) is False

    def test_string_match(self, solution):
        assert solution.string_match("xxcaazz", "xxbaaz") == 3
        assert solution.string_match("abc", "abc") == 2
        assert solution.string_match("abc", "xyz") == 0
        assert solution.string_match("", "") == 0
        assert solution.string_match("ab", "abcd") == 1
