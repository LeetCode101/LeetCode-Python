import unittest
from leetcode.algorithms.p0300_longest_increasing_subsequence_2 import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        solution = Solution()

        self.assertEqual(0, solution.lengthOfLIS([]))
        self.assertEqual(3, solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))
        self.assertEqual(3, solution.lengthOfLIS([10, 9, 2, 5, 3, 4]))
        self.assertEqual(4, solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
