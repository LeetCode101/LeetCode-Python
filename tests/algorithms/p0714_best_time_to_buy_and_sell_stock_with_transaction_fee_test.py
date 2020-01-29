import unittest
from leetcode.algorithms\
    .p0714_best_time_to_buy_and_sell_stock_with_transaction_fee \
    import Solution


class TestBestTimeToBuyAndSellStockWithTransactionFee(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock_with_transaction_fee(self):
        solution = Solution()

        self.assertEqual(0, solution.maxProfit([], 2))
        self.assertEqual(8, solution.maxProfit([1, 3, 2, 8, 4, 9], 2))
