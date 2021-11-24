import unittest
from leetcode.algorithms.p0376_wiggle_subsequence_1 import Solution


class TestWiggleSubsequence(unittest.TestCase):
    def test_wiggle_subsequence(self):
        solution = Solution()

        self.assertEqual(6, solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
        self.assertEqual(7, solution.wiggleMaxLength(
            [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
        self.assertEqual(2, solution.wiggleMaxLength(
            [1, 2, 3, 4, 5, 6, 7, 8, 9]))
