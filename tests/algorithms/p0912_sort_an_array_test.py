import unittest
from leetcode.algorithms.p0912_sort_an_array import Solution


class TestSortAnArray(unittest.TestCase):
    def test_sort_an_array(self):
        solution = Solution()

        self.assertListEqual(
            [0, 0, 1, 1, 2, 5], solution.sortArray([5, 1, 1, 2, 0, 0]))
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6], solution.sortArray([3, 2, 1, 6, 5, 4]))
