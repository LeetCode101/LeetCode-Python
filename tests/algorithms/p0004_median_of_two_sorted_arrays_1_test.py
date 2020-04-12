import unittest
from leetcode.algorithms.p0004_median_of_two_sorted_arrays_1 import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_median_of_two_sorted_arrays(self):
        solution = Solution()

        self.assertEqual(2.0, solution.findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(2.5, solution.findMedianSortedArrays([1, 2], [3, 4]))
        self.assertEqual(2.5, solution.findMedianSortedArrays([3, 4], [1, 2]))
