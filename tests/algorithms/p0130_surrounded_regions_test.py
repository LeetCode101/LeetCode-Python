import unittest
from leetcode.algorithms.p0130_surrounded_regions import Solution


class TestSurroundedRegions(unittest.TestCase):
    def test_surrounded_regions(self):
        solution = Solution()
        board1 = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'],
                  ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
        new_board1 = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
        board2 = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        new_board2 = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        solution.solve(board1)
        solution.solve(board2)

        self.assertListEqual(new_board1, board1)
        self.assertListEqual(new_board2, board2)
