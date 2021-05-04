import unittest
from leetcode.algorithms.p0498_diagonal_traverse_1 import Solution


class TestDiagonalTraverse(unittest.TestCase):
    def test_diagonal_traverse(self):
        solution = Solution()

        self.assertListEqual([], solution.findDiagonalOrder([]))
        self.assertListEqual([1, 2, 4, 7, 5, 3, 6, 8, 9],
                             solution.findDiagonalOrder(
                                 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
