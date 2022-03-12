import unittest
from leetcode.algorithms.p1648_sell_diminishing_valued_colored_balls_2 \
    import Solution


class TestSellDiminishingValuedColoredBalls(unittest.TestCase):
    def test_sell_diminishing_valued_colored_balls(self):
        solution = Solution()

        self.assertEqual(14, solution.maxProfit([2, 5], 4))
        self.assertEqual(19, solution.maxProfit([3, 5], 6))
        self.assertEqual(373219333, solution.maxProfit(
            [497978859, 167261111, 483575207, 591815159], 836556809))
