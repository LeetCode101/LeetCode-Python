import unittest
from leetcode.algorithms.p1216_valid_palindrome_iii_3 import Solution


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = Solution()

        self.assertTrue(solution.isValidPalindrome('', 1))
        self.assertTrue(solution.isValidPalindrome('abcdeca', 2))
        self.assertTrue(solution.isValidPalindrome('abbababa', 1))
