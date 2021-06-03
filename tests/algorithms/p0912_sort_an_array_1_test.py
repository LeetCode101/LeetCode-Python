import unittest
from leetcode.algorithms.p0912_sort_an_array_1 import Solution


class TestSortAnArray(unittest.TestCase):
    def test_sort_an_array(self):
        solution = Solution()

        self.assertListEqual(
            [0, 0, 1, 1, 2, 5], solution.sortArray([5, 1, 1, 2, 0, 0]))
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6], solution.sortArray([3, 2, 1, 6, 5, 4]))
        self.assertListEqual(
            sorted([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]),
            solution.sortArray([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]))
