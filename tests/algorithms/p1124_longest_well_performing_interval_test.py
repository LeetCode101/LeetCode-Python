import unittest
from leetcode.algorithms.p1124_longest_well_performing_interval import Solution


class TestLongestWellPerformingInterval(unittest.TestCase):
    def test_longest_well_performing_interval(self):
        solution = Solution()

        self.assertEqual(6, solution.longestWPI([6, 10, 8, 10, 11, 11]))
        self.assertEqual(3, solution.longestWPI([6, 9, 9]))
        self.assertEqual(1, solution.longestWPI([6, 6, 9]))
        self.assertEqual(3, solution.longestWPI([9, 9, 6, 0, 6, 6, 9]))
        self.assertEqual(0, solution.longestWPI([6, 6, 6]))
