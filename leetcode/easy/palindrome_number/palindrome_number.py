class Solution:
    def is_palindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.
        """
        if x < 0:
            return False
        str_x = str(x)
        for i in range(len(str_x) // 2):
            if str_x[i] != str_x[len(str_x) - i - 1]:
                return False
        return True


## Optimised solution with splicing:
# def is_palindrome(self, x: int) -> bool:
#     if x < 0:
#         return False
#     str_x = str(x)
#     return str_x == str_x[::-1]
