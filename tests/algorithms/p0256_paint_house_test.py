import unittest
from leetcode.algorithms.p0256_paint_house import Solution


class TestPaintHouse(unittest.TestCase):
    def test_paint_house(self):
        solution = Solution()

        self.assertEqual(0, solution.minCost([]))
        self.assertEqual(10, solution.minCost(
            [[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
