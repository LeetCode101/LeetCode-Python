import unittest
from leetcode.algorithms.p0523_continuous_subarray_sum import Solution


class TestContinuousSubarraySum(unittest.TestCase):
    def test_continuous_subarray_sum(self):
        solution = Solution()

        self.assertTrue(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))
        self.assertTrue(solution.checkSubarraySum([23, 2, 6, 4, 7], 6))
        self.assertFalse(solution.checkSubarraySum([23, 2, 6, 4, 7], 9))
