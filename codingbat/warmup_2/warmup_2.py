"""
This file contains all the solutions to problems
covered in "Warmup-2" of CodingBat Python Exercises.
"""


class Solution:
    def string_times(self, s: str, n: int) -> str:
        """
        Return a string that is n copies of the original string.

        Args:
            s (str): The original string.
            n (int): Non-negative number of copies.

        Returns:
            str: The resulting repeated string.
        """
        return s * n

    def front_times(self, s: str, n: int) -> str:
        """
        Return n copies of the front of the string.

        The front of the string is the first 3 characters,
        or the entire string if its length is less than 3.

        Args:
            s (str): The original string.
            n (int): Non-negative number of copies.

        Returns:
            str: The resulting repeated front substring.
        """
        return n * s[:3]

    def string_bits(self, s: str) -> str:
        """
        Return a new string made of every other character starting with the first.

        For example, "Hello" yields "Hlo".

        Args:
            s (str): The original string.

        Returns:
            str: A string made of every other character.
        """
        return s[::2]

    def string_splosion(self, s: str) -> str:
        """
        Return a string made of concatenated prefixes of the input string.

        For example, given "Code", return "CCoCodCode".

        Args:
            s (str): Non-empty input string.

        Returns:
            str: The concatenated string of prefixes.
        """
        parts = []
        for i in range(1, len(s) + 1):
            parts.append(s[:i])
        return "".join(parts)

    # Initial non-optimised solution, for showing difference in complexity between list-join and repeated string concatenation:
    # def string_splosion_old(self, s: str) -> str:
    #     """
    #     Concatenate prefixes of the string using repeated string concatenation.
    #
    #     Args:
    #         s (str): Non-empty input string.
    #
    #     Returns:
    #         str: The concatenated string of prefixes.
    #     """
    #     result = ""
    #     for i in range(len(s) + 1):
    #         result = result + s[:i]
    #     return result
