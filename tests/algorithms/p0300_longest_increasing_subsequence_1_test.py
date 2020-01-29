import unittest
from leetcode.algorithms.p0300_longest_increasing_subsequence_1 import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        solution = Solution()

        self.assertEqual(0, solution.lengthOfLIS([]))
        self.assertEqual(4, solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
