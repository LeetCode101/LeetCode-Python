import unittest
from leetcode.algorithms.p0053_maximum_subarray_1 import Solution


class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_subarray(self):
        solution = Solution()

        self.assertEqual(
            6, solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
