import unittest
from leetcode.algorithms.p0040_combination_sum_ii import Solution


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        solution = Solution()

        self.assertListEqual(sorted([
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]), solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
