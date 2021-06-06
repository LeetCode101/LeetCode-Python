import unittest
from leetcode.algorithms.p0216_combination_sum_iii import Solution


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        solution = Solution()

        self.assertListEqual(
            sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
            solution.combinationSum3(3, 9))
