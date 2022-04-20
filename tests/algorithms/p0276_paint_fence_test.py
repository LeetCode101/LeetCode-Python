import unittest
from leetcode.algorithms.p0276_paint_fence import Solution


class TestPaintFence(unittest.TestCase):
    def test_paint_fence(self):
        solution = Solution()

        self.assertEqual(0, solution.numWays(0, 1))
        self.assertEqual(1, solution.numWays(1, 1))
        self.assertEqual(6, solution.numWays(3, 2))
        self.assertEqual(42, solution.numWays(7, 2))
