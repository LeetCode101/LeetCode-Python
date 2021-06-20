import unittest
from leetcode.algorithms.p0829_consecutive_numbers_sum_1 import Solution


class TestConsecutiveNumbersSum(unittest.TestCase):
    def test_consecutive_numbers_sum(self):
        solution = Solution()

        self.assertEqual(2, solution.consecutiveNumbersSum(5))
        self.assertEqual(4, solution.consecutiveNumbersSum(15))
