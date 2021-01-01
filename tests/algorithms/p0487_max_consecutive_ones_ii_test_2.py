import unittest
from leetcode.algorithms.p0487_max_consecutive_ones_ii_2 import Solution


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones(self):
        solution = Solution()

        self.assertEqual(2, solution.findMaxConsecutiveOnes(
            [0, 1]))
        self.assertEqual(1, solution.findMaxConsecutiveOnes(
            [1]))
        self.assertEqual(4, solution.findMaxConsecutiveOnes(
            [1, 1, 0, 1]))
        self.assertEqual(4, solution.findMaxConsecutiveOnes(
            [1, 0, 1, 1, 0]))
