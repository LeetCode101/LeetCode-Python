import unittest
from leetcode.algorithms.p1682_longest_palindromic_subsequence_ii \
    import Solution


class TestLongestPalindromicSubsequence(unittest.TestCase):
    def test_longest_palindromic_subsequence(self):
        solution = Solution()

        self.assertEqual(0, solution.longestPalindromeSubseq(''))
        self.assertEqual(4, solution.longestPalindromeSubseq('bbabab'))
        self.assertEqual(4, solution.longestPalindromeSubseq('dcbccacdb'))
