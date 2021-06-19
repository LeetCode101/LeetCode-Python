import unittest
from leetcode.algorithms.p0862_shortest_subarray_with_sum_at_least_k_1 \
    import Solution


class TestShortestSubarrayWithSumAtLeastK(unittest.TestCase):
    def test_shortest_subarray_with_sum_at_least_k(self):
        solution = Solution()

        self.assertEqual(1, solution.shortestSubarray([1], 1))
        self.assertEqual(3, solution.shortestSubarray([2, -1, 2], 3))
