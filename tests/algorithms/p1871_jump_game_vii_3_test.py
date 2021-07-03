import unittest
from leetcode.algorithms.p1871_jump_game_vii_3 import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertFalse(solution.canReach('0000000000', 8, 8))
        self.assertFalse(solution.canReach('', 1, 1))
        self.assertTrue(solution.canReach('011010', 2, 3))
        self.assertFalse(solution.canReach('01101110', 2, 3))
