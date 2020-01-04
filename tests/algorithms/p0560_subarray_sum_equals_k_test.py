import unittest
from leetcode.algorithms.p0560_subarray_sum_equals_k_1 \
    import Solution as Solution1
from leetcode.algorithms.p0560_subarray_sum_equals_k_2 \
    import Solution as Solution2


class TestSubarraySumEqualsK(unittest.TestCase):
    def test_subarray_sum_equals_k1(self):
        solution = Solution1()

        self.assertEqual(2, solution.subarraySum([1, 1, 1], 2))
        self.assertEqual(1, solution.subarraySum([1, 2, 1], 2))

    def test_subarray_sum_equals_k2(self):
        solution = Solution2()

        self.assertEqual(2, solution.subarraySum([1, 1, 1], 2))
        self.assertEqual(1, solution.subarraySum([1, 2, 1], 2))
