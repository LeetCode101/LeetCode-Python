import unittest
from leetcode.algorithms.p0698_partition_to_k_equal_sum_subsets_2 \
    import Solution


class TestPartitionToKEqualSumSubsets(unittest.TestCase):
    def test_partition_to_k_equal_sum_subsets(self):
        solution = Solution()

        self.assertTrue(solution.canPartitionKSubsets(
            [1, 1, 1, 1, 2, 2, 2, 2], 2))
        self.assertFalse(solution.canPartitionKSubsets(
            [2, 2, 2, 2, 3, 4, 5], 4))
        self.assertTrue(solution.canPartitionKSubsets(
            [4, 3, 2, 3, 5, 2, 1], 4))
        self.assertFalse(solution.canPartitionKSubsets([1, 2, 3, 4], 3))
