import unittest
from leetcode.algorithms.p0377_combination_sum_iv import Solution


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum(self):
        solution = Solution()

        # self.assertEqual(7, solution.combinationSum4([1, 2, 3], 4))
        self.assertEqual(1, solution.combinationSum4([4, 2, 1], 28))
