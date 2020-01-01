import unittest
from leetcode.algorithms.p1099_two_sum_less_than_k import Solution


class TestTwoSumLessThanK(unittest.TestCase):
    def test_two_sum_less_than_k(self):
        solution = Solution()

        self.assertEqual(58, solution.twoSumLessThanK(
            [34, 23, 1, 24, 75, 33, 54, 8], 60))
        self.assertEqual(-1, solution.twoSumLessThanK([10, 20, 30], 15))
