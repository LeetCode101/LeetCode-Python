import unittest
from leetcode.algorithms.p1066_campus_bikes_ii import Solution


class TestCampusBikes(unittest.TestCase):
    def test_campus_bikes(self):
        solution = Solution()

        self.assertEqual(6, solution.assignBikes(
            [[0, 0], [2, 1]], [[1, 2], [3, 3]]))
        self.assertEqual(4, solution.assignBikes(
            [[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))
