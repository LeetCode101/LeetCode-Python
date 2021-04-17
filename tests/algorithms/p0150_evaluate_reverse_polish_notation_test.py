import unittest
from leetcode.algorithms.p0150_evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test_evaluate_reverse_polish_notation(self):
        solution = Solution()

        self.assertEqual(0, solution.evalRPN(['1', '1', '-']))
        self.assertEqual(22, solution.evalRPN(
            ['10', '6', '9', '3', '+', '-11', '*',
             '/', '*', '17', '+', '5', '+']))
