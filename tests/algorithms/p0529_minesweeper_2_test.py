import unittest
from leetcode.algorithms.p0529_minesweeper_2 import Solution


class TestMinesweeper(unittest.TestCase):
    def test_minesweeper(self):
        solution = Solution()

        self.assertListEqual(
            [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],
            solution.updateBoard(
                [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],
                [3, 0]))
        self.assertListEqual(
            [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'],
             ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],
            solution.updateBoard(
                [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'],
                 ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],
                [1, 2]))
