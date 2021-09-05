import unittest
from leetcode.algorithms.p0674_longest_continuous_increasing_subsequence \
    import Solution


class TestLongestContinuousIncreasingSubsequence(unittest.TestCase):
    def test_longest_continuous_increasing_subsequence(self):
        solution = Solution()

        self.assertEqual(3, solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
        self.assertEqual(1, solution.findLengthOfLCIS([2, 2, 2, 2, 2]))
