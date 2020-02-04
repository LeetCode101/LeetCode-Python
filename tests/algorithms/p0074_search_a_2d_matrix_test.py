import unittest
from leetcode.algorithms.p0074_search_a_2d_matrix import Solution


class TestSearchA2DMatrix(unittest.TestCase):
    def test_search_a_2d_matrix(self):
        solution = Solution()
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]

        self.assertTrue(solution.searchMatrix(matrix, 3))
        self.assertFalse(solution.searchMatrix(matrix, 13))
