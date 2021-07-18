import unittest
from leetcode.algorithms.p0918_maximum_sum_circular_subarray import Solution


class TestMaximumSumCircularSubarray(unittest.TestCase):
    def test_maximum_sum_circular_subarray(self):
        solution = Solution()

        self.assertEqual(3, solution.maxSubarraySumCircular([1, -2, 3, -2]))
        self.assertEqual(4, solution.maxSubarraySumCircular([3, -1, 2, -1]))
