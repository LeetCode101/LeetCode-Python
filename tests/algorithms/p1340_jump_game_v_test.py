import unittest
from leetcode.algorithms.p1340_jump_game_v import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertEqual(4, solution.maxJumps(
            [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
        self.assertEqual(2, solution.maxJumps([7, 1, 7, 1, 7, 1], 2))
