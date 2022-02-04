import unittest
from leetcode.algorithms.p1197_minimum_knight_moves_2 import Solution


class TestMinimumKnightMoves(unittest.TestCase):
    def test_minimum_knight_moves(self):
        solution = Solution()

        self.assertEqual(1, solution.minKnightMoves(2, 1))
        self.assertEqual(4, solution.minKnightMoves(5, 5))
