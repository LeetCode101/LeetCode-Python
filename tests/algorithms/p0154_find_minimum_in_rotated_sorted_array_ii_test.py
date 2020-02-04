import unittest
from leetcode\
    .algorithms.p0154_find_minimum_in_rotated_sorted_array_ii import Solution


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def test_find_minimum_in_rotated_sorted_array(self):
        solution = Solution()

        self.assertEqual(1, solution.findMin([3, 3, 1, 3]))
        self.assertEqual(1, solution.findMin([1, 3, 5]))
        self.assertEqual(0, solution.findMin([2, 2, 2, 0, 1]))
