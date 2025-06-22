import pytest
from palindrome_number import Solution


@pytest.fixture
def solution():
    return Solution()


class TestPalindrome:
    def test_cases(self, solution):
        assert solution.isPalindrome(121)
        assert not solution.isPalindrome(122)
        assert not solution.isPalindrome(-121)
        assert solution.isPalindrome(1)
