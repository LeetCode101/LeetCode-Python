import unittest
from leetcode.algorithms.p0282_expression_add_operators import Solution


class TestExpressionAddOperators(unittest.TestCase):
    def test_expression_add_operators(self):
        solution = Solution()

        self.assertListEqual(['1*2*3', '1+2+3'], solution.addOperators('123', 6))
        self.assertListEqual(['2*3+2', '2+3*2'], solution.addOperators('232', 8))
        self.assertListEqual(['1*0+5', '10-5'], solution.addOperators('105', 5))
