import unittest
from leetcode.algorithms.p1143_longest_common_subsequence import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_longest_common_subsequence(self):
        solution = Solution()

        self.assertEqual(3, solution.longestCommonSubsequence('abcde', 'ace'))
        self.assertEqual(3, solution.longestCommonSubsequence('abc', 'abc'))
