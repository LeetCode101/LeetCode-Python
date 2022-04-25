import unittest
from leetcode.algorithms.p0416_partition_equal_subset_sum import Solution


class TestPartitionEqualSubsetSum(unittest.TestCase):
    def test_partition_equal_subset_sum(self):
        solution = Solution()

        self.assertTrue(solution.canPartition([1, 5, 11, 5]))
        self.assertFalse(solution.canPartition([1, 2, 3, 5]))
