import unittest
from leetcode.algorithms.p0279_perfect_squares import Solution


class TestPerfectSquares(unittest.TestCase):
    def test_perfect_squares(self):
        solution = Solution()

        self.assertEqual(3, solution.numSquares(12))
        self.assertEqual(2, solution.numSquares(13))
