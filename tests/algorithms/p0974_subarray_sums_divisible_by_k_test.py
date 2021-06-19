import unittest
from leetcode.algorithms.p0974_subarray_sums_divisible_by_k import Solution


class TestSubarraySumsDivisibleByK(unittest.TestCase):
    def test_subarray_sums_divisible_by_k(self):
        solution = Solution()

        self.assertEqual(7, solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
