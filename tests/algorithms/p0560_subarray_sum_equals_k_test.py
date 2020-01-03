import unittest
from leetcode.algorithms.p0560_subarray_sum_equals_k_1 import Solution as Solution1


class TestSubarraySumEqualsK(unittest.TestCase):
    def test_subarray_sum_equals_k1(self):
        solution = Solution1()

        self.assertEqual(2, solution.subarraySum([1, 1, 1], 2))
