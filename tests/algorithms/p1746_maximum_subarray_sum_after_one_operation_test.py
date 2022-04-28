import unittest
from leetcode.algorithms.p1746_maximum_subarray_sum_after_one_operation \
    import Solution


class TestMaximumSubarraySumAfterOneOperation(unittest.TestCase):
    def test_maximum_subarray_sum_after_one_operation(self):
        solution = Solution()

        self.assertEqual(17, solution.maxSumAfterOperation([2, -1, -4, -3]))
        self.assertEqual(4, solution.maxSumAfterOperation(
            [1, -1, 1, 1, -1, -1, 1]))
