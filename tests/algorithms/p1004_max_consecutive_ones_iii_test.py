import unittest
from leetcode.algorithms.p1004_max_consecutive_ones_iii import Solution


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones(self):
        solution = Solution()

        self.assertEqual(
            6, solution.longestOnes(
                [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
