import unittest
from leetcode.algorithms.p0680_valid_palindrome_ii import Solution


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = Solution()

        self.assertTrue(solution.validPalindrome('aba'))
        self.assertTrue(solution.validPalindrome('abca'))
        self.assertFalse(solution.validPalindrome('abc'))
        self.assertTrue(solution.validPalindrome('deeee'))
