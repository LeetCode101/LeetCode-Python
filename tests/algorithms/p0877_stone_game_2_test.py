import unittest
from leetcode.algorithms.p0877_stone_game_2 import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertTrue(solution.stoneGame([5, 3, 4, 5]))
        self.assertTrue(solution.stoneGame([3, 7, 2, 3]))
