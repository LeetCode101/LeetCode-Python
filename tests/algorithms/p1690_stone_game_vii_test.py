import unittest
from leetcode.algorithms.p1690_stone_game_vii import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual(6, solution.stoneGameVII([5, 3, 1, 4, 2]))
        self.assertEqual(122, solution.stoneGameVII(
            [7, 90, 5, 1, 100, 10, 10, 2]))
