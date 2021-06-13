import unittest
from leetcode.algorithms.p0084_largest_rectangle_in_histogram import Solution


class TestLargestRectangleInHistogram(unittest.TestCase):
    def test_largest_rectangle_in_histogram(self):
        solution = Solution()

        self.assertEqual(10, solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
