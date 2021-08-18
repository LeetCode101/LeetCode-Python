import unittest
from leetcode.algorithms.p1040_moving_stones_until_consecutive_ii \
    import Solution


class TestMovingStonesUntilConsecutive(unittest.TestCase):
    def test_moving_stones_until_consecutive(self):
        solution = Solution()

        self.assertListEqual([1, 2], solution.numMovesStonesII([7, 4, 9]))
        self.assertListEqual([2, 3], solution.numMovesStonesII(
            [6, 5, 4, 3, 10]))
