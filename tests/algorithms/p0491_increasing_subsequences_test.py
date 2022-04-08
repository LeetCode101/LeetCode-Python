import unittest
from leetcode.algorithms.p0491_increasing_subsequences import Solution


class TestIncreasingSubsequences(unittest.TestCase):
    def test_increasing_subsequences(self):
        solution = Solution()

        self.assertListEqual(
            [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7],
             [6, 7], [6, 7, 7], [7, 7]],
            solution.findSubsequences([4, 6, 7, 7]))
        self.assertListEqual([[4, 4]], solution.findSubsequences(
            [4, 4, 3, 2, 1]))
