import unittest
from leetcode.algorithms.p1137_n_th_tribonacci_number import Solution


class TestNthTribonacciNumber(unittest.TestCase):
    def test_n_th_tribonacci_number(self):
        solution = Solution()

        self.assertEqual(0, solution.tribonacci(0))
        self.assertEqual(1, solution.tribonacci(1))
        self.assertEqual(1, solution.tribonacci(2))
        self.assertEqual(4, solution.tribonacci(4))
        self.assertEqual(1389537, solution.tribonacci(25))
