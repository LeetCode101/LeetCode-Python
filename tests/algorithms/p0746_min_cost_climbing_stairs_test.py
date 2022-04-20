import unittest
from leetcode.algorithms.p0746_min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        solution = Solution()

        self.assertEqual(15, solution.minCostClimbingStairs([10, 15, 20]))
        self.assertEqual(6, solution.minCostClimbingStairs(
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
