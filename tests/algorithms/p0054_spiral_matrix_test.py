import unittest
from leetcode.algorithms.p0054_spiral_matrix import Solution


class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):
        solution = Solution()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.assertListEqual([], solution.spiralOrder([]))
        self.assertListEqual([6, 9, 7], solution.spiralOrder([[6, 9, 7]]))
        self.assertListEqual(
            [1, 2, 3, 6, 9, 8, 7, 4, 5], solution.spiralOrder(matrix))
