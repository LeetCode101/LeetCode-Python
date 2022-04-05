import unittest
from leetcode.algorithms \
    .p2099_find_subsequence_of_length_k_with_the_largest_sum import Solution


class TestFindSubsequenceOfLengthKWithTheLargestSum(unittest.TestCase):
    def test_find_subsequence_of_length_k_with_the_largest_sum(self):
        solution = Solution()

        self.assertListEqual([3, 3], solution.maxSubsequence([2, 1, 3, 3], 2))
        self.assertListEqual([-1, 3, 4], solution.maxSubsequence(
            [-1, -2, 3, 4], 3))
        self.assertListEqual([4, 3], solution.maxSubsequence([3, 4, 3, 3], 2))
