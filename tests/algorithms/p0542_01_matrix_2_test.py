import unittest
from leetcode.algorithms.p0542_01_matrix_2 import Solution


class Test01Matrix(unittest.TestCase):
    def test_01_matrix(self):
        solution = Solution()

        self.assertListEqual([], solution.updateMatrix([]))
        self.assertListEqual([[0, 0, 0], [0, 1, 0], [1, 2, 1]],
                             solution.updateMatrix(
                                 [[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
