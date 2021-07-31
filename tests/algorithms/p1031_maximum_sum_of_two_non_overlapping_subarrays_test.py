import unittest
from leetcode.algorithms.p1031_maximum_sum_of_two_non_overlapping_subarrays \
    import Solution


class TestMaximumSumOfTwoNonOverlappingSubarrays(unittest.TestCase):
    def test_maximum_sum_of_two_non_overlapping_subarrays(self):
        solution = Solution()

        self.assertEqual(20, solution.maxSumTwoNoOverlap(
            [0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
        self.assertEqual(31, solution.maxSumTwoNoOverlap(
            [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
