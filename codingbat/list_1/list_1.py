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

    def reverse3(self, nums: list[int]) -> list[int]:
        """Return an array with the elements in reverse order.

        Given an array of integers of length 3, return a new array with
        the elements in reverse order. For example, [1, 2, 3] becomes [3, 2, 1].

        Args:
            nums (list[int]): A list of 3 integers.

        Returns:
            list[int]: A new list with the elements reversed.
        """
        return nums[::-1]

    def max_end3(self, nums: list[int]) -> list[int]:
        """
        Given an array of ints length 3, replace all elements with
        the larger of the first or last element, and return the new array.

        Args:
            nums (list[int]): A list of exactly 3 integers.

        Returns:
            list[int]: A new list of length 3, where every element
            equals the larger of the first or last element.
        """
        big = max(nums[0], nums[-1])
        return [big] * 3

    def sum2(self, nums: list[int]) -> int:
        """
        Return the sum of the first two elements of a list of integers.
        If the list has fewer than two elements, return the sum of
        the elements that exist. If the list is empty, return 0.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The sum of the first two elements, or sum of all elements
                 if fewer than two exist.
        """
        return sum(nums[:2])

    def middle_way(self, a: list[int], b: list[int]) -> list[int]:
        """
        Return a new list containing the middle elements of two input lists,
        each of length 3.

        Args:
            a (list[int]): The first input list of length 3.
            b (list[int]): The second input list of length 3.

        Returns:
            list[int]: A list of length 2 containing [middle of a, middle of b].
        """
        return [a[1], b[1]]

    def make_ends(self, nums: list[int]) -> list[int]:
        """
        Return a new list containing the first and last elements of the input list.

        Args:
            nums (list[int]): The input list of integers (length >= 1).

        Returns:
            list[int]: A list of length 2 containing [first element, last element].
        """
        return [nums[0], nums[-1]]

    def has23(self, nums: list[int]) -> bool:
        """
        Return True if the input list of length 2 contains a 2 or a 3.

        Args:
            nums (list[int]): A list of two integers.

        Returns:
            bool: True if 2 or 3 is present in the list, False otherwise.
        """
        return 2 in nums or 3 in nums
