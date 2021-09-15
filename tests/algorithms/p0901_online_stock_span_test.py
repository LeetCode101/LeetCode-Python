import unittest
from leetcode.algorithms.p0901_online_stock_span import StockSpanner


class TestOnlineStockSpan(unittest.TestCase):
    def test_online_stock_span(self):
        stock_spanner = StockSpanner()

        self.assertEqual(1, stock_spanner.next(100))
        self.assertEqual(1, stock_spanner.next(80))
        self.assertEqual(1, stock_spanner.next(60))
        self.assertEqual(2, stock_spanner.next(70))
        self.assertEqual(1, stock_spanner.next(60))
        self.assertEqual(4, stock_spanner.next(75))
        self.assertEqual(6, stock_spanner.next(85))
