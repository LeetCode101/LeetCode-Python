import unittest
from leetcode.algorithms.p1696_jump_game_vi_3 import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertEqual(0, solution.maxResult([], 1))
        self.assertEqual(7, solution.maxResult([1, -1, -2, 4, -7, 3], 2))
        self.assertEqual(17, solution.maxResult([10, -5, -2, 4, 0, 3], 3))
