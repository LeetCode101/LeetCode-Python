import unittest
from leetcode.algorithms.p0857_minimum_cost_to_hire_k_workers import Solution


class TestMinimumCostToHireKWorkers(unittest.TestCase):
    def test_minimum_cost_to_hire_k_workers(self):
        solution = Solution()

        self.assertTrue(abs(solution.mincostToHireWorkers(
            [10, 20, 5], [70, 50, 30], 2) - 105) < 0.01)
        self.assertTrue(abs(solution.mincostToHireWorkers(
            [3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3) - 30.667) < 0.01)
