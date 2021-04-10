import unittest
from leetcode.algorithms.p1473_paint_house_iii import Solution


class TestPaintHouse(unittest.TestCase):
    def test_paint_house(self):
        solution = Solution()

        self.assertEqual(9, solution.minCost(
            [0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            5, 2, 3))
        self.assertEqual(-1, solution.minCost(
            [3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
            4, 3, 3))
