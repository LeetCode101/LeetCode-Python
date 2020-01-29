import unittest
from leetcode.algorithms.p0188_best_time_to_buy_and_sell_stock_iv \
    import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        solution = Solution()

        self.assertEqual(0, solution.maxProfit(2, []))
        self.assertEqual(2, solution.maxProfit(2, [2, 4, 1]))
        self.assertEqual(7, solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))
        self.assertEqual(7, solution.maxProfit(100, [3, 2, 6, 5, 0, 3]))
