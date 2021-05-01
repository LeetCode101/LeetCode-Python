import unittest
from leetcode.algorithms.p0772_basic_calculator_iii import Solution


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        solution = Solution()

        self.assertEqual(-12, solution.calculate('(2+6*3+5-(3*14/7+2)*5)+3'))
