import unittest
from leetcode.algorithms.p0240_search_a_2d_matrix_ii import Solution


class TestSearchA2DMatrix(unittest.TestCase):
    def test_search_a_2d_matrix(self):
        solution = Solution()
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]

        self.assertFalse(solution.searchMatrix([], 1))
        self.assertFalse(solution.searchMatrix([[]], 1))
        self.assertTrue(solution.searchMatrix(matrix, 5))
        self.assertFalse(solution.searchMatrix(matrix, 20))
