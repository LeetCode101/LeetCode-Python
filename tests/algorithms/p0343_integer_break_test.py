import unittest
from leetcode.algorithms.p0343_integer_break import Solution


class TestIntegerBreak(unittest.TestCase):
    def test_integer_break(self):
        solution = Solution()

        self.assertEqual(1, solution.integerBreak(2))
        self.assertEqual(36, solution.integerBreak(10))
