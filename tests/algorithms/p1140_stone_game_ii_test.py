import unittest
from leetcode.algorithms.p1140_stone_game_ii import Solution


class TestStoneGame(unittest.TestCase):
    def test_stone_game(self):
        solution = Solution()

        self.assertEqual(10, solution.stoneGameII([2, 7, 9, 4, 4]))
        self.assertEqual(104, solution.stoneGameII([1, 2, 3, 4, 5, 100]))
        self.assertEqual(479, solution.stoneGameII(
            [94, 65, 70, 79, 91, 80, 21, 67, 84, 64, 34, 22, 14, 10, 72]))
