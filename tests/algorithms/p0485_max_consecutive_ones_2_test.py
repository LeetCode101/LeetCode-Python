import unittest
from leetcode.algorithms.p0485_max_consecutive_ones_2 import Solution


class TestMaxConsecutiveOnes(unittest.TestCase):
    def test_max_consecutive_ones(self):
        solution = Solution()

        self.assertEqual(3, solution.findMaxConsecutiveOnes(
            [1, 1, 0, 1, 1, 1]))
