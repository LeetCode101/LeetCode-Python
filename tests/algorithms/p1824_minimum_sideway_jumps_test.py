import unittest
from leetcode.algorithms.p1824_minimum_sideway_jumps import Solution


class TestMinimumSidewayJumps(unittest.TestCase):
    def test_minimum_sideway_jumps(self):
        solution = Solution()

        self.assertEqual(2, solution.minSideJumps([0, 1, 2, 3, 0]))
        self.assertEqual(0, solution.minSideJumps([0, 1, 1, 3, 3, 0]))
        self.assertEqual(2, solution.minSideJumps([0, 2, 1, 0, 3, 0]))
