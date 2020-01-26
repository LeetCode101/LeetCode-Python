import unittest
from leetcode.algorithms.p0050_pow_2 import Solution


class TestPow(unittest.TestCase):
    def test_pow(self):
        solution = Solution()

        self.assertEqual(1, solution.myPow(0.44528, 0))
        self.assertEqual(1024.0, solution.myPow(2.0, 10))
        self.assertEqual(0.25, solution.myPow(2.0, -2))
