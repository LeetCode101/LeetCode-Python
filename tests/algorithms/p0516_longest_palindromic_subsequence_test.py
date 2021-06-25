import unittest
from leetcode.algorithms.p0516_longest_palindromic_subsequence import Solution


class TestLongestPalindromicSubsequence(unittest.TestCase):
    def test_longest_palindromic_subsequence(self):
        solution = Solution()

        self.assertEqual(0, solution.longestPalindromeSubseq(''))
        self.assertEqual(4, solution.longestPalindromeSubseq('bbbab'))
        self.assertEqual(2, solution.longestPalindromeSubseq('cbbd'))
