import unittest
from leetcode.algorithms.p0410_split_array_largest_sum import Solution


class TestSplitArrayLargestSum(unittest.TestCase):
    def test_split_array_largest_sum(self):
        solution = Solution()

        self.assertEqual(18, solution.splitArray([7, 2, 5, 10, 8], 2))
