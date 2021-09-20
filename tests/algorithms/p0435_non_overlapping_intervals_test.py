import unittest
from leetcode.algorithms.p0435_non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def test_non_overlapping_intervals(self):
        solution = Solution()

        self.assertEqual(0, solution.eraseOverlapIntervals([]))
        self.assertEqual(1, solution.eraseOverlapIntervals(
            [[1, 2], [2, 3], [3, 4], [1, 3]]))
        self.assertEqual(2, solution.eraseOverlapIntervals(
            [[1, 2], [1, 2], [1, 2]]))
        self.assertEqual(0, solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
