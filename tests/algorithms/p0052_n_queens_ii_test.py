import unittest
from leetcode.algorithms.p0052_n_queens_ii import Solution


class TestNQueens(unittest.TestCase):
    def test_n_queens(self):
        solution = Solution()

        self.assertEqual(2, solution.totalNQueens(4))
