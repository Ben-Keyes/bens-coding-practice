"""
This file contains all the solutions to problems
covered in "Warmup-1" of CodingBat Python Exercises
"""


class Solution:
    def sleep_in(self, weekday: bool, vacation: bool) -> bool:
        """
        The parameter weekday is True if it is a weekday,
        and the parameter vacation is True if we are on vacation.
        We sleep in if it is not a weekday, or we're on vacation.
        Return True if we sleep in.
        """
        return not weekday or vacation

    def monkey_trouble(self, a_smile: bool, b_smile: bool) -> bool:
        """
        We have two monkeys, a and b,
        and the parameters a_smile and b_smile indicate if each is smiling.
        We are in trouble if they are both smiling or if neither of them is smiling.
        Return True if we are in trouble.
        """
        return a_smile == b_smile

    def sum_double(self, a: int, b: int) -> int:
        """
        Given two int values, return their sum. Unless the two values are the same,
        then return double their sum.
        """
        return 2 * (a + b) if a == b else a + b

    def diff21(self, n: int) -> int:
        """
        Given an int n, return the absolute difference between n and 21,
        except return double the absolute difference if n is over 21.
        """
        return abs(n - 21) * 2 if n > 21 else abs(n - 21)

    def parrot_trouble(self, talking: bool, hour: int) -> bool:
        """
        We have a loud talking parrot.
        The "hour" parameter is the current hour time in the range 0..23.
        We are in trouble if the parrot is talking and the hour is before 7 or after 20.
        Return True if we are in trouble.
        """
        return talking and (hour < 7 or hour > 20)

    def makes10(self, a: int, b: int) -> bool:
        """
        Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
        """
        return (a == 10 or b == 10) or (a + b == 10)

    def near_hundred(self, n: int) -> bool:
        """
        Given an int n, return True if it is within 10 of 100 or 200.
        """
        return abs(100 - n) <= 10 or abs(200 - n) <= 10

    def pos_neg(self, a: int, b: int, negative: bool) -> bool:
        """
        Given 2 int values, return True if one is negative and one is positive.
        Except if the parameter "negative" is True,
        then return True only if both are negative.
        """
        if negative:
            return a < 0 and b < 0
        return (a > 0 > b) or (a < 0 < b)

    def not_string(self, s: str) -> str:
        """
        Given a string, return a new string where "not " has been added to the front.
        However, if the string already begins with "not", return the string unchanged.
        """
        return s if s.startswith("not") else "not " + s

    def missing_char(self, s: str, n: int) -> str:
        """
        Given a non-empty string and an int n,
        return a new string where the char at index n has been removed.
        The value of n will be a valid index of a char in the original string
        (i.e. n will be in the range 0...len(str)-1 inclusive).
        """
        return s[:n] + s[n + 1 :]

    def front_back(self, s: str) -> str:
        """
        Given a string, return a new string where the first
        and last chars have been exchanged.
        """
        return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]

    def front3(self, s: str) -> str:
        """
        Given a string, we'll say that the front is the first 3 chars of the string.
        If the string length is less than 3, the front is whatever is there.
        Return a new string which is 3 copies of the front.
        """
        front = s[:3]
        return front * 3
