import unittest
from leetcode.algorithms.p0908_smallest_range_i import Solution


class TestSmallestRange(unittest.TestCase):
    def test_smallest_range(self):
        solution = Solution()

        self.assertEqual(6, solution.smallestRangeI([0, 10], 2))
        self.assertEqual(0, solution.smallestRangeI([1, 3, 6], 3))
