"""
This file contains all the solutions to problems
covered in "List-1" of CodingBat Python Exercises.
"""


class Solution:
    def first_last6(self, nums: list[int]) -> bool:
        """
        Return True if 6 appears as either the first or last element in the list.

        The list will have at least one element.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if 6 is the first or last element, False otherwise.
        """
        return nums[0] == 6 or nums[-1] == 6

    def same_first_last(self, nums: list[int]) -> bool:
        """
        Return True if the list has length 1 or more and its
        first and last elements are the same.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if the list has at least one element and
            the first and last elements are equal, otherwise False.
        """
        return len(nums) >= 1 and nums[0] == nums[-1]

    def make_pi(self) -> list[int]:
        """Return a list containing the first 3 digits of pi: [3, 1, 4].

        Returns:
            list[int]: A list with the integers [3, 1, 4].
        """
        return [3, 1, 4]

    def common_end(self, a: list[int], b: list[int]) -> bool:
        """
        Return True if the two lists have the same first element or
        the same last element. Both lists have length 1 or more.

        Args:
            a (list[int]): The first input list.
            b (list[int]): The second input list.

        Returns:
            bool: True if the first elements are equal or the last elements are equal,
            False otherwise.
        """
        return a[0] == b[0] or a[-1] == b[-1]

    def sum3(self, nums: list[int]) -> int:
        """
        Return the sum of all elements in a list of exactly 3 integers.

        Args:
            nums (list[int]): A list of exactly 3 integers.

        Returns:
            int: The sum of the three integers.
        """
        return sum(nums)

    def rotate_left3(self, nums: list[int]) -> list[int]:
        """Return an array with the elements rotated left.

        For a given list of length 3, the first element is moved to
        the end, and the other elements shift left.

        Args:
            nums (list[int]): A list of exactly 3 integers.

        Returns:
            list[int]: The rotated list.
        """
        return nums[1:] + nums[:1]
