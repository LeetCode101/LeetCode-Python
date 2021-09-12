import unittest
from leetcode.algorithms.p0263_ugly_number import Solution


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        solution = Solution()

        self.assertTrue(solution.isUgly(6))
        self.assertTrue(solution.isUgly(8))
        self.assertTrue(solution.isUgly(14))
        self.assertTrue(solution.isUgly(1))
