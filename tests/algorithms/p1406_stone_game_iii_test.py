import unittest
from leetcode.algorithms.p1406_stone_game_iii import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual('Tie', solution.stoneGameIII([-1, -2, -3]))
        self.assertEqual('Bob', solution.stoneGameIII([1, 2, 3, 7]))
        self.assertEqual('Alice', solution.stoneGameIII([1, 2, 3, -9]))
        self.assertEqual('Tie', solution.stoneGameIII([1, 2, 3, 6]))
