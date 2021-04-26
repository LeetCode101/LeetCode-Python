import unittest
from leetcode.algorithms.p0224_basic_calculator import Solution


class TestBasicCalculator(unittest.TestCase):
    def test_basic_calculator(self):
        solution = Solution()

        self.assertEqual(2147483647, solution.calculate('2147483647'))
        self.assertEqual(23, solution.calculate('(1+(4+5+2)-3)+(6+8)'))
