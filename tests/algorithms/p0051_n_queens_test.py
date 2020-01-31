import unittest
from leetcode.algorithms.p0051_n_queens import Solution


class TestNQueens(unittest.TestCase):
    def test_n_queens(self):
        solution = Solution()
        expected_lists = [
            ['.Q..', '...Q', 'Q...', '..Q.'],
            ['..Q.', 'Q...', '...Q', '.Q..']
        ]
        actual_lists = solution.solveNQueens(4)

        self.assertListEqual(expected_lists, actual_lists)
