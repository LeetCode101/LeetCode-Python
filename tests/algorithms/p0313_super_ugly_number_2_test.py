import unittest
from leetcode.algorithms.p0313_super_ugly_number_2 import Solution


class TestSuperUglyNumber(unittest.TestCase):
    def test_super_ugly_number(self):
        solution = Solution()

        self.assertEqual(32, solution.nthSuperUglyNumber(12, [2, 7, 13, 19]))
        self.assertEqual(1, solution.nthSuperUglyNumber(1, [2, 3, 5]))
