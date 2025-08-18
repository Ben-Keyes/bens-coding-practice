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

    def last2(self, s: str) -> int:
        """
        Count the number of times a substring of length 2 appears in the string
        and also matches the last 2 characters of the string.

        This does not count the substring at the very end of the string.

        Args:
            s (str): The input string.

        Returns:
            int: The count of matching substrings.

        Examples:
            >>> self.last2("hixxxhi")
            1
            >>> self.last2("hellohello")
            1
            >>> self.last2("hi")
            0
        """
        if len(s) < 2:
            return 0
        matches = (s[i : i + 2] == s[-2:] for i in range(len(s) - 2))
        return sum(matches)

    def array_count9(self, nums: list[int]) -> int:
        """
        Count the number of 9's in a list of integers.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The count of 9's in the list.

        Notes:
            You could also solve this using ``nums.count(9)``,
            but the generator version works on any iterable,
            not just lists.
        """
        return sum(x == 9 for x in nums)

    def array_front9(self, nums: list[int]) -> bool:
        """
        Return True if there is a 9 in the first 4 elements of the list.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if 9 is present in the first 4 elements, False otherwise.

        Notes:
            A cleaner answer would be:
            ``return any(x == 9 for x in nums[:4])``.
            However, CodingBat doesn't support the 'any' function.
        """
        for x in nums[:4]:
            if x == 9:
                return True
        return False

    def array123(self, nums: list[int]) -> bool:
        """
        Return True if there is a 1,2,3 sequence in the list.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if the sequence "1,2,3" is present in the list, False otherwise.

        Notes:
            Again, a cleaner answer would be:
            ``return any(nums[i:i+3] == [1,2,3] for i in range(len(nums) - 2))``.
            However, CodingBat doesn't support the 'any' function.

            Also, unlike my solution, directly comparing integers may be slightly more efficient...
            e.g. ``if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:``
            Not a noticeable impact for the exercise, but in longer lists would be preferable.
        """
        for i in range(len(nums) - 2):
            if nums[i : i + 3] == [1, 2, 3]:
                return True
        return False

    def string_match(self, a: str, b: str) -> int:
        """
        Counts the number of positions where the two strings
        contain the same length-2 substring.

        A length-2 substring is a consecutive sequence of 2 characters in a string.
        For example, in "hello", the length-2 substrings are "he", "el", "ll", "lo".

        The function compares substrings at the same positions in both strings
        and counts how many are equal.

        Args:
            a (str): The first input string.
            b (str): The second input string.

        Returns:
            int: The number of positions where a and b have the same length-2 substring.

        Example:
            string_match("xxcaazz", "xxbaaz") returns 3
            because the matching substrings are "xx", "aa", and "az".
        """
        length = min(len(a), len(b))
        return sum(a[i : i + 2] == b[i : i + 2] for i in range(length - 1))
