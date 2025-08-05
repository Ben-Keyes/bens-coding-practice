import pytest
from palindrome_number import Solution


@pytest.fixture
def solution():
    return Solution()


class TestPalindrome:
    def test_cases(self, solution):
        assert solution.is_palindrome(121)
        assert not solution.is_palindrome(122)
        assert not solution.is_palindrome(-121)
        assert solution.is_palindrome(1)
