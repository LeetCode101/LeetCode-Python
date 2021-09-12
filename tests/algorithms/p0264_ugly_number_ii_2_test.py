import unittest
from leetcode.algorithms.p0264_ugly_number_ii_2 import Solution


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        solution = Solution()

        self.assertEqual(12, solution.nthUglyNumber(10))
        self.assertEqual(1, solution.nthUglyNumber(1))
