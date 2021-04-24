import unittest
from leetcode.algorithms.p0494_target_sum_1 import Solution


class TestTargetSum(unittest.TestCase):
    def test_target_sum(self):
        solution = Solution()

        self.assertEqual(5, solution.findTargetSumWays([1, 1, 1, 1, 1], 3))
