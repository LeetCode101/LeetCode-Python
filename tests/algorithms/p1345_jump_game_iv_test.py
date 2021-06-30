import unittest
from leetcode.algorithms.p1345_jump_game_iv import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertEqual(3, solution.minJumps(
            [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
        self.assertEqual(1, solution.minJumps([7, 6, 9, 6, 9, 6, 9, 7]))
        self.assertEqual(0, solution.minJumps([]))
