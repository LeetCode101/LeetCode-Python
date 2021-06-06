import unittest
from leetcode.algorithms.p0039_combination_sum_1 import Solution


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        solution = Solution()

        self.assertListEqual(
            sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            solution.combinationSum([2, 3, 5], 8))
