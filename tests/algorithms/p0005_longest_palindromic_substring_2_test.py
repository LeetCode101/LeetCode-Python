import unittest
from leetcode.algorithms.p0005_longest_palindromic_substring_2 import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_longest_palindromic_substring(self):
        solution = Solution()

        self.assertEqual('bb', solution.longestPalindrome('cbbd'))
        self.assertEqual('bab', solution.longestPalindrome('babad'))
        self.assertEqual('bb', solution.longestPalindrome('cbbd'))
