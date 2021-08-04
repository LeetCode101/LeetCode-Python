import unittest
from leetcode.algorithms.p0910_smallest_range_ii import Solution


class TestSmallestRange(unittest.TestCase):
    def test_smallest_range(self):
        solution = Solution()

        self.assertEqual(6, solution.smallestRangeII([0, 10], 2))
        self.assertEqual(3, solution.smallestRangeII([1, 3, 6], 3))
