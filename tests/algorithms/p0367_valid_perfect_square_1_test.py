import unittest
from leetcode.algorithms.p0367_valid_perfect_square_1 import Solution


class TestValidPerfectSquare(unittest.TestCase):
    def test_valid_perfect_square(self):
        solution = Solution()

        self.assertTrue(solution.isPerfectSquare(16))
        self.assertFalse(solution.isPerfectSquare(14))
