import unittest
from leetcode.algorithms.p1510_stone_game_iv import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertTrue(solution.winnerSquareGame(1))
        self.assertFalse(solution.winnerSquareGame(2))
        self.assertFalse(solution.winnerSquareGame(17))
