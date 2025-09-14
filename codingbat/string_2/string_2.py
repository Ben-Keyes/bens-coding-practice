"""
This file contains all the solutions to problems
covered in "String-2" of CodingBat Python Exercises.
"""


class Solution:
    def double_char(self, s: str) -> str:
        """
        Return a string where each character in the input string
        appears twice in a row.

        Args:
            s (str): The input string.

        Returns:
            str: A new string with each character doubled.
        """
        return "".join(ch * 2 for ch in s)
