import unittest
from leetcode.algorithms.p1563_stone_game_v import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual(18, solution.stoneGameV([6, 2, 3, 4, 5, 5]))
        self.assertEqual(28, solution.stoneGameV([7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual(0, solution.stoneGameV([4]))
        self.assertEqual(1103936, solution.stoneGameV(
            [62008, 269055, 379802, 503405, 589774]))
