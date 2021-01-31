import unittest
from leetcode.algorithms.p0283_move_zeroes_2 import Solution


class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        solution = Solution()
        numbers = [0, 1, 0, 3, 12]
        solution.moveZeroes(numbers)

        self.assertListEqual([1, 3, 12, 0, 0], numbers)
