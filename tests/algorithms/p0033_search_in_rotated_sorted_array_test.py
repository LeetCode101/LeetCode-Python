import unittest
from leetcode.algorithms.p0033_search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        solution = Solution()

        self.assertEqual(-1, solution.search([5, 1, 3], 0))
        self.assertEqual(2, solution.search([5, 1, 3], 3))
        self.assertEqual(4, solution.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, solution.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(-1, solution.search([4, 5, 6, 7, 0, 1, 2], 10))
