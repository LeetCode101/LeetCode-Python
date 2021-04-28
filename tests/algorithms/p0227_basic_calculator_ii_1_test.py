import unittest
from leetcode.algorithms.p0227_basic_calculator_ii_1 import Solution


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        solution = Solution()

        self.assertEqual(1, solution.calculate('3-2'))
        self.assertEqual(7, solution.calculate('3+2*2'))
        self.assertEqual(5, solution.calculate(' 3+5 / 2 '))
