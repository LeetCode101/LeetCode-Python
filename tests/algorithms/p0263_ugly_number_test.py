import unittest
from leetcode.algorithms.p0263_ugly_number import Solution


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        solution = Solution()

        self.assertFalse(solution.isUgly(0))
        self.assertTrue(solution.isUgly(6))
        self.assertTrue(solution.isUgly(8))
        self.assertFalse(solution.isUgly(14))
        self.assertTrue(solution.isUgly(1))
