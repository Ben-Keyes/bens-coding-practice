"""
This file contains all the solutions to problems
covered in "Warmup-1" of CodingBat Python Exercises.
"""


class Solution:
    def sleep_in(self, weekday: bool, vacation: bool) -> bool:
        """
        Determine if we sleep in.

        We sleep in if it is not a weekday or if we are on vacation.

        Args:
            weekday (bool): True if it is a weekday.
            vacation (bool): True if we are on vacation.

        Returns:
            bool: True if we sleep in, False otherwise.
        """
        return not weekday or vacation

    def monkey_trouble(self, a_smile: bool, b_smile: bool) -> bool:
        """
        Determine if we are in trouble because of monkeys smiling.

        We are in trouble if both monkeys are smiling or neither is smiling.

        Args:
            a_smile (bool): True if monkey a is smiling.
            b_smile (bool): True if monkey b is smiling.

        Returns:
            bool: True if we are in trouble, False otherwise.
        """
        return a_smile == b_smile

    def sum_double(self, a: int, b: int) -> int:
        """
        Return sum of two integers, or double the sum if the integers are the same.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            int: Sum or double sum if values are equal.
        """
        return 2 * (a + b) if a == b else a + b

    def diff21(self, n: int) -> int:
        """
        Compute the absolute difference between n and 21.

        Return double the absolute difference if n is over 21.

        Args:
            n (int): The integer to compare with 21.

        Returns:
            int: Absolute difference or double absolute difference.
        """
        return abs(n - 21) * 2 if n > 21 else abs(n - 21)

    def parrot_trouble(self, talking: bool, hour: int) -> bool:
        """
        Determine if we are in trouble because of a talking parrot.

        We are in trouble if the parrot is talking and the hour is before 7 or after 20.

        Args:
            talking (bool): True if the parrot is talking.
            hour (int): Current hour in range 0..23.

        Returns:
            bool: True if we are in trouble, False otherwise.
        """
        return talking and (hour < 7 or hour > 20)

    def makes10(self, a: int, b: int) -> bool:
        """
        Check if either integer is 10 or their sum is 10.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            bool: True if condition holds, False otherwise.
        """
        return (a == 10 or b == 10) or (a + b == 10)

    def near_hundred(self, n: int) -> bool:
        """
        Determine if n is within 10 of 100 or 200.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if n is within 10 of 100 or 200, False otherwise.
        """
        return abs(100 - n) <= 10 or abs(200 - n) <= 10

    def pos_neg(self, a: int, b: int, negative: bool) -> bool:
        """
        Determine if one integer is positive and the other negative.

        If negative is True, return True only if both are negative.

        Args:
            a (int): First integer.
            b (int): Second integer.
            negative (bool): Condition flag.

        Returns:
            bool: True if conditions are met, False otherwise.
        """
        if negative:
            return a < 0 and b < 0
        return (a > 0 > b) or (a < 0 < b)

    def not_string(self, s: str) -> str:
        """
        Add "not " to the front of the string unless it already starts with "not".

        Args:
            s (str): Original string.

        Returns:
            str: Modified string with "not " prefixed if needed.
        """
        return s if s.startswith("not") else "not " + s

    def missing_char(self, s: str, n: int) -> str:
        """
        Remove the character at index n from the string.

        Args:
            s (str): Original string.
            n (int): Index of character to remove.

        Returns:
            str: String with character at n removed.
        """
        return s[:n] + s[n + 1 :]

    def front_back(self, s: str) -> str:
        """
        Swap the first and last characters of the string.

        Args:
            s (str): Original string.

        Returns:
            str: String with first and last characters swapped.
        """
        return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]

    def front3(self, s: str) -> str:
        """
        Return 3 copies of the front of the string.

        The front is the first 3 characters, or whatever is there if the string is shorter than 3.

        Args:
            s (str): Original string.

        Returns:
            str: New string made of 3 copies of the front.
        """
        front = s[:3]
        return front * 3
