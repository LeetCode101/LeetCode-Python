import unittest
from leetcode.algorithms.p1033_moving_stones_until_consecutive import Solution


class TestMovingStonesUntilConsecutive(unittest.TestCase):
    def test_moving_stones_until_consecutive(self):
        solution = Solution()

        self.assertListEqual([1, 2], solution.numMovesStones(1, 2, 5))
        self.assertListEqual([0, 0], solution.numMovesStones(4, 3, 2))
        self.assertListEqual([1, 2], solution.numMovesStones(3, 5, 1))
