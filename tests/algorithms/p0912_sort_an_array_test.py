import unittest
from leetcode.algorithms.p0912_sort_an_array import Solution


class TestSortAnArray(unittest.TestCase):
    def test_sort_an_array(self):
        solution = Solution()

        self.assertListEqual(sorted([5, 1, 1, 2, 0, 0]),
                             solution.sortArray([5, 1, 1, 2, 0, 0]))
