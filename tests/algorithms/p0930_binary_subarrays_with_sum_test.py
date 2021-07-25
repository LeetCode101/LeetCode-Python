import unittest
from leetcode.algorithms.p0930_binary_subarrays_with_sum import Solution


class TestBinarySubarraysWithSum(unittest.TestCase):
    def test_binary_subarrays_with_sum(self):
        solution = Solution()

        self.assertEqual(4, solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
        self.assertEqual(15, solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
