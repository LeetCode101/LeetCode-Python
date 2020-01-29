import unittest
from leetcode.algorithms.p0322_coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def test_coin_change(self):
        solution = Solution()

        self.assertEqual(3, solution.coinChange([1, 2, 5], 11))
        self.assertEqual(-1, solution.coinChange([2], 3))
