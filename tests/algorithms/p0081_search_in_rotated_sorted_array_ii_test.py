import unittest
from leetcode.algorithms.p0081_search_in_rotated_sorted_array_ii \
    import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        solution = Solution()

        self.assertTrue(solution.search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertTrue(solution.search([2, 5, 6, 0, 0, 1, 2], 1))
        self.assertFalse(solution.search([2, 5, 6, 0, 0, 1, 2], 3))
        self.assertFalse(solution.search([2, 5, 6, 0, 0, 1, 2], 10))
