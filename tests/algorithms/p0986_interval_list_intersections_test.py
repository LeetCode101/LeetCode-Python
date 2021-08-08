import unittest
from leetcode.algorithms.p0986_interval_list_intersections import Solution


class TestIntervalListIntersections(unittest.TestCase):
    def test_interval_list_intersections(self):
        solution = Solution()

        self.assertListEqual(
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
            solution.intervalIntersection(
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]]))
        self.assertListEqual([], solution.intervalIntersection(
            [[1, 3], [5, 9]], []))
