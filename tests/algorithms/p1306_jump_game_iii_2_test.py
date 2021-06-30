import unittest
from leetcode.algorithms.p1306_jump_game_iii_2 import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertTrue(solution.canReach([4, 2, 3, 0, 3, 1, 2], 5))
        self.assertFalse(solution.canReach([3, 0, 2, 1, 2], 2))
