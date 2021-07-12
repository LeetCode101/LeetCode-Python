import unittest
from leetcode.algorithms\
    .p0153_find_minimum_in_rotated_sorted_array import Solution


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def test_find_minimum_in_rotated_sorted_array(self):
        solution = Solution()

        self.assertEqual(1, solution.findMin([3, 4, 5, 1, 2]))
        self.assertEqual(0, solution.findMin([4, 5, 6, 7, 0, 1, 2]))
