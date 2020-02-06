import unittest
from leetcode.algorithms.p0121_best_time_to_buy_and_sell_stock_2 \
    import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        solution = Solution()

        self.assertEqual(0, solution.maxProfit([]))
        self.assertEqual(5, solution.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, solution.maxProfit([7, 6, 4, 3, 1]))
