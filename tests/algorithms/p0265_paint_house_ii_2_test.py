import unittest
from leetcode.algorithms.p0265_paint_house_ii_2 import Solution


class TestPaintHouse(unittest.TestCase):
    def test_paint_house(self):
        solution = Solution()

        self.assertEqual(0, solution.minCostII([]))
        self.assertEqual(5, solution.minCostII([[1, 5, 3], [2, 9, 4]]))
