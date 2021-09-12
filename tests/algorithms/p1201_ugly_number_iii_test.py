import unittest
from leetcode.algorithms.p1201_ugly_number_iii import Solution


class TestUglyNumber(unittest.TestCase):
    def test_ugly_number(self):
        solution = Solution()

        self.assertEqual(4, solution.nthUglyNumber(3, 2, 3, 5))
        self.assertEqual(6, solution.nthUglyNumber(4, 2, 3, 4))
        self.assertEqual(10, solution.nthUglyNumber(5, 2, 11, 13))
