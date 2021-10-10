import unittest
from leetcode.algorithms.p1057_campus_bikes import Solution


class TestCampusBikes(unittest.TestCase):
    def test_campus_bikes(self):
        solution = Solution()

        self.assertListEqual([1, 0], solution.assignBikes(
            [[0, 0], [2, 1]], [[1, 2], [3, 3]]))
        self.assertListEqual([0, 2, 1], solution.assignBikes(
            [[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))
