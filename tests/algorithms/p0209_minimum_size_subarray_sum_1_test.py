import unittest
from leetcode.algorithms.p0209_minimum_size_subarray_sum_1 import Solution


class TestMinimumSizeSubarraySum(unittest.TestCase):
    def test_minimum_size_subarray_sum(self):
        solution = Solution()

        self.assertEqual(0, solution.minSubArrayLen(1, []))
        self.assertEqual(2, solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
        self.assertEqual(0, solution.minSubArrayLen(
            11, [1, 1, 1, 1, 1, 1, 1, 1]))
