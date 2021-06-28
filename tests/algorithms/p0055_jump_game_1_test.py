import unittest
from leetcode.algorithms.p0055_jump_game_1 import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertTrue(solution.canJump([]))
        self.assertTrue(solution.canJump([2, 3, 1, 1, 4]))
        self.assertFalse(solution.canJump([3, 2, 1, 0, 4]))
