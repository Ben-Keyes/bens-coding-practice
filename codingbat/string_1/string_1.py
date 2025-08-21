"""
This file contains all the solutions to problems
covered in "String-1" of CodingBat Python Exercises.
"""


class Solution:
    def hello_name(self, name: str) -> str:
        """
        Return a greeting in the form 'Hello name!'.

        Args:
            name (str): The input name.

        Returns:
            str: A greeting message in the form "Hello {name}!".
        """
        return f"Hello {name}!"

    def make_abba(self, a: str, b: str) -> str:
        """
        Return a string in the form abba.

        Concatenates two input strings in the order abba, e.g.
        "Hi" and "Bye" returns "HiByeByeHi".

        Args:
            a (str): The first input string.
            b (str): The second input string.

        Returns:
            str: A new string in the form abba.
        """
        return f"{a}{b}{b}{a}"

    def make_tags(self, tag: str, word: str) -> str:
        """
        Wrap a word with the given HTML tag.

        This function generates an HTML string by surrounding the input
        word with the specified tag. For example, if the tag is "i" and
        the word is "Yay", the result will be "<i>Yay</i>".

        Args:
            tag (str): The HTML tag name (without angle brackets).
            word (str): The word or text to wrap inside the HTML tag.

        Returns:
            str: A string containing the word wrapped with the given tag.
        """
        return f"<{tag}>{word}</{tag}>"

    def make_out_word(self, out: str, word: str) -> str:
        """
        Inserts a word into the middle of a 4-character 'out' string.

        The 'out' string is assumed to be length 4. The function places
        the 'word' between the first two and last two characters of 'out'.

        Args:
            out (str): A string of length 4, e.g. "<<>>".
            word (str): The word to insert into the middle of 'out'.

        Returns:
            str: The new string with 'word' inserted in the middle of 'out'.
        """
        return out[:2] + word + out[2:4]

    def extra_end(self, s: str) -> str:
        """
        Returns a new string made of 3 copies of the last 2 characters
        of the input string. Assumes the string length is at least 2.

        Args:
            s (str): The input string.

        Returns:
            str: A new string made of 3 copies of the last 2 characters.
        """
        return s[-2:] * 3

    def first_two(self, s: str) -> str:
        """
        Return a string made of the first two characters of the input string.

        If the string has fewer than two characters, return the string as-is.

        Args:
            s (str): The input string.

        Returns:
            str: A string made of the first two characters, or the whole string
            if it has fewer than two characters.
        """
        return s[:2]

    def first_half(self, s: str) -> str:
        """
        Return the first half of a string of even length.

        Args:
            s (str): Input string of even length.

        Returns:
            str: The first half of the string.
        """
        return s[: len(s) // 2]
