import unittest
from leetcode.algorithms.p0560_subarray_sum_equals_k_2 \
    import Solution


class TestSubarraySumEqualsK(unittest.TestCase):
    def test_subarray_sum_equals_k(self):
        solution = Solution()

        self.assertEqual(2, solution.subarraySum([1, 1, 1], 2))
        self.assertEqual(1, solution.subarraySum([1, 2, 1], 2))
