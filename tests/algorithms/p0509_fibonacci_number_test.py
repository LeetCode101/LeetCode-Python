import unittest
from leetcode.algorithms.p0509_fibonacci_number import Solution


class TestFibonacciNumber(unittest.TestCase):
    def test_fibonacci_number(self):
        solution = Solution()

        self.assertEqual(1, solution.fib(1))
        self.assertEqual(1, solution.fib(2))
        self.assertEqual(2, solution.fib(3))
