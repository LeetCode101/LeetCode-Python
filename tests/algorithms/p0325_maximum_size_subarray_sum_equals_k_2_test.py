import unittest
from leetcode.algorithms.p0325_maximum_size_subarray_sum_equals_k_2 \
    import Solution


class TestMaximumSizeSubarraySumEqualsK(unittest.TestCase):
    def test_maximum_size_subarray_sum_equals_k(self):
        solution = Solution()

        self.assertEqual(0, solution.maxSubArrayLen([], 1))
        self.assertEqual(4, solution.maxSubArrayLen([1, -1, 5, -2, 3], 3))
        self.assertEqual(2, solution.maxSubArrayLen([-2, -1, 2, 1], 1))
