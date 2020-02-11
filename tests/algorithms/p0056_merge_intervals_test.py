import unittest
from leetcode.algorithms.p0056_merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        solution = Solution()

        self.assertListEqual([], solution.merge([]))
        self.assertListEqual([[1, 5]], solution.merge([[1, 4], [4, 5]]))
        self.assertListEqual(
            [[1, 6], [8, 10], [15, 18]],
            solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
