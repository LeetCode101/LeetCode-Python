import unittest
from leetcode.algorithms.p0633_sum_of_square_numbers_1 import Solution


class TestSumOfSquareNumbers(unittest.TestCase):
    def test_sum_of_square_numbers(self):
        solution = Solution()

        self.assertTrue(solution.judgeSquareSum(4))
        self.assertTrue(solution.judgeSquareSum(5))
        self.assertFalse(solution.judgeSquareSum(3))
