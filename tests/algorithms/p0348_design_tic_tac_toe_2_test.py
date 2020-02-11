import unittest
from leetcode.algorithms.p0348_design_tic_tac_toe_2 import TicTacToe


class TestDesignTicTacToe(unittest.TestCase):
    def test_design_tic_tac_toe(self):
        tic_tac_toe = TicTacToe(3)
        tic_tac_toe2 = TicTacToe(2)
        tic_tac_toe3 = TicTacToe(2)
        tic_tac_toe4 = TicTacToe(2)

        self.assertEqual(0, tic_tac_toe.move(0, 0, 1))
        self.assertEqual(0, tic_tac_toe.move(0, 2, 2))
        self.assertEqual(0, tic_tac_toe.move(2, 2, 1))
        self.assertEqual(0, tic_tac_toe.move(1, 1, 2))
        self.assertEqual(0, tic_tac_toe.move(2, 0, 1))
        self.assertEqual(0, tic_tac_toe.move(1, 0, 2))
        self.assertEqual(1, tic_tac_toe.move(2, 1, 1))
        self.assertEqual(0, tic_tac_toe2.move(0, 0, 2))
        self.assertEqual(0, tic_tac_toe2.move(0, 1, 1))
        self.assertEqual(2, tic_tac_toe2.move(1, 1, 2))
        self.assertEqual(0, tic_tac_toe3.move(0, 0, 2))
        self.assertEqual(0, tic_tac_toe3.move(0, 1, 1))
        self.assertEqual(2, tic_tac_toe3.move(1, 0, 2))
        self.assertEqual(0, tic_tac_toe4.move(0, 1, 2))
        self.assertEqual(0, tic_tac_toe4.move(0, 0, 1))
        self.assertEqual(2, tic_tac_toe4.move(1, 0, 2))
