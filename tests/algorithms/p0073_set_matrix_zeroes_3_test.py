import unittest
from leetcode.algorithms.p0073_set_matrix_zeroes_3 import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    def test_set_matrix_zeroes(self):
        solution = Solution()
        actual_lists = [
          [0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]
        ]
        actual_lists2 = []
        expected_lists = [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
        solution.setZeroes(actual_lists)
        solution.setZeroes(actual_lists2)

        self.assertListEqual(expected_lists, actual_lists)
        self.assertListEqual([], actual_lists2)
