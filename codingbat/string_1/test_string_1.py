import pytest
from string_1 import Solution


@pytest.fixture
def solution():
    return Solution()


class TestString1:
    def test_hello_name(self, solution):
        assert solution.hello_name("Bob") == "Hello Bob!"
        assert solution.hello_name("Alice") == "Hello Alice!"
        assert solution.hello_name("") == "Hello !"
        assert solution.hello_name("X") == "Hello X!"
        assert solution.hello_name("123") == "Hello 123!"

    def test_make_abba(self, solution):
        assert solution.make_abba("Hi", "Bye") == "HiByeByeHi"
        assert solution.make_abba("Yo", "Alice") == "YoAliceAliceYo"
        assert solution.make_abba("a", "b") == "abba"
        assert solution.make_abba("", "Y") == "YY"
        assert solution.make_abba("AB", "") == "ABAB"

    def test_make_tags(self, solution):
        assert solution.make_tags("i", "Yay") == "<i>Yay</i>"
        assert solution.make_tags("b", "Hello") == "<b>Hello</b>"
        assert solution.make_tags("p", "") == "<p></p>"
        assert solution.make_tags("h1", "Welcome") == "<h1>Welcome</h1>"
        assert solution.make_tags("span", "text") == "<span>text</span>"

    def test_make_out_word(self, solution):
        assert solution.make_out_word("<<>>", "Yay") == "<<Yay>>"
        assert solution.make_out_word("[[]]", "Hello") == "[[Hello]]"
        assert solution.make_out_word("{{}}", "Python") == "{{Python}}"
        assert solution.make_out_word("****", "Hi") == "**Hi**"
        assert solution.make_out_word("!!@@", "Test") == "!!Test@@"

    def test_extra_end(self, solution):
        assert solution.extra_end("Hello") == "lololo"
        assert solution.extra_end("ab") == "ababab"
        assert solution.extra_end("Hi") == "HiHiHi"
        assert solution.extra_end("Python") == "ononon"
        assert solution.extra_end("Code") == "dedede"

    def test_first_two(self, solution):
        assert solution.first_two("Hello") == "He"
        assert solution.first_two("abcdef") == "ab"
        assert solution.first_two("X") == "X"
        assert solution.first_two("") == ""
        assert solution.first_two("Hi") == "Hi"

    def test_first_half(self, solution):
        assert solution.first_half("WooHoo") == "Woo"
        assert solution.first_half("HelloThere") == "Hello"
        assert solution.first_half("Hi") == "H"
        assert solution.first_half("AB") == "A"
        assert solution.first_half("PythonTree") == "Pytho"

    def test_without_end(self, solution):
        assert solution.without_end("Hello") == "ell"
        assert solution.without_end("ab") == ""
        assert solution.without_end("python") == "ytho"
        assert solution.without_end("coding") == "odin"
        assert solution.without_end("12345") == "234"

    def test_combo_string(self, solution):
        assert solution.combo_string("Hello", "hi") == "hiHellohi"
        assert solution.combo_string("hi", "Hello") == "hiHellohi"
        assert solution.combo_string("a", "xyz") == "axyza"
        assert solution.combo_string("", "abc") == "abc"
        assert solution.combo_string("kitten", "dog") == "dogkittendog"

    def test_non_start(self, solution):
        assert solution.non_start("Hello", "There") == "ellohere"
        assert solution.non_start("java", "code") == "avaode"
        assert solution.non_start("shotl", "java") == "hotlava"
        assert solution.non_start("a", "x") == ""
        assert solution.non_start("ab", "xy") == "by"

    def test_left2(self, solution):
        assert solution.left2("Hello") == "lloHe"
        assert solution.left2("java") == "vaja"
        assert solution.left2("Hi") == "Hi"
        assert solution.left2("Code") == "deCo"
        assert solution.left2("Python") == "thonPy"
