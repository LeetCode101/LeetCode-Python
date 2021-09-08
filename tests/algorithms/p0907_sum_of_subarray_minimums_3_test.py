import unittest
from leetcode.algorithms.p0907_sum_of_subarray_minimums_3 import Solution


class TestSumOfSubarrayMinimums(unittest.TestCase):
    def test_sum_of_subarray_minimums(self):
        solution = Solution()

        self.assertEqual(17, solution.sumSubarrayMins([3, 1, 2, 4]))
        self.assertEqual(444, solution.sumSubarrayMins([11, 81, 94, 43, 3]))
