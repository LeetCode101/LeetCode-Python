import unittest
from leetcode.algorithms.p1686_stone_game_vi import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual(1, solution.stoneGameVI([1, 3], [2, 1]))
        self.assertEqual(0, solution.stoneGameVI([1, 2], [3, 1]))
        self.assertEqual(-1, solution.stoneGameVI([2, 4, 3], [1, 6, 7]))
