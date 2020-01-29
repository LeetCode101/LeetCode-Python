import unittest
from leetcode.algorithms.p0309_best_time_to_buy_and_sell_stock_with_cooldown \
    import Solution


class TestBestTimeToBuyAndSellStockWithCooldown(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock_with_cooldown(self):
        solution = Solution()

        self.assertEqual(0, solution.maxProfit([]))
        self.assertEqual(1, solution.maxProfit([1, 2]))
        self.assertEqual(3, solution.maxProfit([1, 2, 3, 0, 2]))
