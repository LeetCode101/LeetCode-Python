import unittest
from leetcode.algorithms.p0763_partition_labels import Solution


class TestPartitionLabels(unittest.TestCase):
    def test_partition_labels(self):
        solution = Solution()

        self.assertListEqual([9, 7, 8], solution.partitionLabels(
            'ababcbacadefegdehijhklij'))
        self.assertListEqual([10], solution.partitionLabels('eccbbbbdec'))
