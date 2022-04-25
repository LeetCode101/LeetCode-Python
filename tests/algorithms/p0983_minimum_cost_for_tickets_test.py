import unittest
from leetcode.algorithms.p0983_minimum_cost_for_tickets import Solution


class TestMinimumCostForTickets(unittest.TestCase):
    def test_minimum_cost_for_tickets(self):
        solution = Solution()

        self.assertEqual(11, solution.mincostTickets(
            [1, 4, 6, 7, 8, 20], [2, 7, 15]))
        self.assertEqual(17, solution.mincostTickets(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
