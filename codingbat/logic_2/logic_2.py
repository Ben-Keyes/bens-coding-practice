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
