import unittest
from leetcode.algorithms.p0045_jump_game_ii import Solution


class TestJumpGame(unittest.TestCase):
    def test_jump_game(self):
        solution = Solution()

        self.assertEqual(2, solution.jump(
            [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))
        self.assertEqual(2, solution.jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, solution.jump([2, 3, 0, 1, 4]))
