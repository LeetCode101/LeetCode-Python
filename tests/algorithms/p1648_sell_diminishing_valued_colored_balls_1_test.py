import unittest
from leetcode.algorithms.p1648_sell_diminishing_valued_colored_balls_1 \
    import Solution


class TestSellDiminishingValuedColoredBalls(unittest.TestCase):
    def test_sell_diminishing_valued_colored_balls(self):
        solution = Solution()

        self.assertEqual(1, solution.maxProfit([1], 2))
        self.assertEqual(14, solution.maxProfit([2, 5], 4))
        self.assertEqual(19, solution.maxProfit([3, 5], 6))
