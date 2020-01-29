import unittest
from leetcode.algorithms.p0123_best_time_to_buy_and_sell_stock_iii \
    import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        solution = Solution()

        self.assertEqual(0, solution.maxProfit([]))
        self.assertEqual(6, solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
        self.assertEqual(4, solution.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, solution.maxProfit([7, 6, 4, 3, 1]))
