import unittest
from leetcode.algorithms.p1872_stone_game_viii import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual(5, solution.stoneGameVIII([-1, 2, -3, 4, -5]))
        self.assertEqual(13, solution.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]))
        self.assertEqual(-22, solution.stoneGameVIII([-10, -12]))
