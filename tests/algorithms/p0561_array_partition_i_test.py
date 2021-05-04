import unittest
from leetcode.algorithms.p0561_array_partition_i import Solution


class TestArrayPartition(unittest.TestCase):
    def test_array_partition(self):
        solution = Solution()

        self.assertEqual(4, solution.arrayPairSum([1, 4, 3, 2]))
