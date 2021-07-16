import unittest
from leetcode.algorithms\
    .p1477_find_two_non_overlapping_sub_arrays_each_with_target_sum_3 \
    import Solution


class TestFindTwoNonOverlappingSubArraysEachWithTargetSum(unittest.TestCase):
    def test_find_two_non_overlapping_sub_arrays_each_with_target_sum(self):
        solution = Solution()

        self.assertEqual(-1, solution.minSumOfLengths([1, 6, 1], 7))
        self.assertEqual(2, solution.minSumOfLengths([3, 2, 2, 4, 3], 3))
        self.assertEqual(-1, solution.minSumOfLengths(
            [4, 3, 2, 6, 2, 3, 4], 6))
