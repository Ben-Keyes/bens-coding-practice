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

    def without_end(self, s: str) -> str:
        """
        Return a string with the first and last characters removed.

        The input string must have a length of at least 2.
        For example, "Hello" yields "ell".

        Args:
            s (str): The input string (length >= 2).

        Returns:
            str: The string without its first and last characters.
        """
        return s[1:-1]

    def combo_string(self, a: str, b: str) -> str:
        """
        Return a string of the form short+long+short, with the shorter string on the
        outside and the longer string on the inside.

        If one string is shorter than the other, the shorter one goes on both sides
        of the longer string. The input strings will not be the same length, but
        either one may be empty.

        Args:
            a (str): The first input string.
            b (str): The second input string.

        Returns:
            str: A new string in the form short+long+short.
        """
        short, long = (a, b) if len(a) < len(b) else (b, a)
        return short + long + short

    def non_start(self, a: str, b: str) -> str:
        """Concatenate two strings without their first characters.

        This function removes the first character from each input string
        and returns the concatenation of the resulting substrings.

        Args:
            a (str): The first input string (at least length 1).
            b (str): The second input string (at least length 1).

        Returns:
            str: The concatenated string without the first character of each input.
        """
        return a[1:] + b[1:]

    def left2(self, s: str) -> str:
        """Return a string with the first 2 characters moved to the end.

        This performs a "left rotation" of 2 characters. The string length
        will be at least 2.

        Args:
            s (str): The input string (length >= 2).

        Returns:
            str: The rotated string.
        """
        return s[2:] + s[:2]
