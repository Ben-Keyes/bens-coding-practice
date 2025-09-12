"""
This file contains all the solutions to problems
covered in "Logic-2" of CodingBat Python Exercises.
"""


class Solution:

    def make_bricks(self, small: int, big: int, goal: int) -> bool:
        """
        Determine if a goal length can be reached using small and big bricks.

        Rules:
            - Small bricks are 1 inch each.
            - Big bricks are 5 inches each.
            - Return True if it is possible to reach exactly the goal length.

        Args:
            small (int): The number of small bricks available.
            big (int): The number of big bricks available.
            goal (int): The target length in inches.

        Returns:
            bool: True if the goal can be reached, False otherwise.
        """
        return goal % 5 <= small and goal <= small + big * 5

    def lone_sum(self, a: int, b: int, c: int) -> int:
        """
        Calculate the sum of three integers, excluding duplicates.

        Rules:
            - If a value appears more than once, it does not count toward the sum.

        Args:
            a (int): The first integer.
            b (int): The second integer.
            c (int): The third integer.

        Returns:
            int: The sum of unique values among a, b, and c.
        """
        return (
            (a if a != b and a != c else 0)
            + (b if b != a and b != c else 0)
            + (c if c != a and c != b else 0)
        )

    def lucky_sum(self, a: int, b: int, c: int) -> int:
        """
        Calculate the sum of three integers with a special rule for 13.

        Rules:
            - If a is 13, return 0.
            - If b is 13, return a.
            - If c is 13, return a + b.
            - Otherwise return a + b + c.

        Args:
            a (int): The first integer.
            b (int): The second integer.
            c (int): The third integer.

        Returns:
            int: The sum according to the special rules.
        """
        if a == 13:
            return 0
        if b == 13:
            return a
        if c == 13:
            return a + b
        return a + b + c

    def no_teen_sum(self, a: int, b: int, c: int) -> int:
        """
        Calculate the sum of three integers, treating most teen values as 0.

        Rules:
            - Values in the range 13..19 count as 0.
            - Exceptions: 15 and 16 are not treated as teens.

        Args:
            a (int): The first integer.
            b (int): The second integer.
            c (int): The third integer.

        Returns:
            int: The sum after applying the teen rule.
        """
        return self.fix_teen(a) + self.fix_teen(b) + self.fix_teen(c)

    def fix_teen(self, n: int) -> int:
        """
        Fix a value according to the teen rule.

        Args:
            n (int): The integer to fix.

        Returns:
            int: 0 if n is a teen (13..19, excluding 15 and 16), else n.
        """
        return 0 if 13 <= n <= 19 and n not in {15, 16} else n

    def round_sum(self, a: int, b: int, c: int) -> int:
        """
        Calculate the sum of three integers, rounding each to the nearest multiple of 10.

        Rules:
            - If the rightmost digit is 5 or more, round up.
            - Otherwise, round down.
            - Use a helper function to avoid repetition.

        Args:
            a (int): The first integer.
            b (int): The second integer.
            c (int): The third integer.

        Returns:
            int: The sum of the rounded values.
        """
        return self.round10(a) + self.round10(b) + self.round10(c)

    def round10(self, num: int) -> int:
        """
        Round a number to the nearest multiple of 10.

        Args:
            num (int): The number to round.

        Returns:
            int: num rounded to the nearest multiple of 10.
        """
        return num + (10 - num % 10 if num % 10 >= 5 else -(num % 10))

    def make_chocolate(self, small: int, big: int, goal: int) -> int:
        """
        Determine the number of small bars needed to reach the goal weight.

        Always use as many big bars (5 kilos each) as possible before using small bars (1 kilo each).
        If it is not possible to meet the goal with the given bars, return -1.

        Args:
            small (int): The number of available small bars (1 kilo each).
            big (int): The number of available big bars (5 kilos each).
            goal (int): The target weight in kilos.

        Returns:
            int: The number of small bars needed, or -1 if the goal cannot be met.
        """
        max_big = min(goal // 5, big)
        remainder = goal - max_big * 5
        return remainder if remainder <= small else -1
