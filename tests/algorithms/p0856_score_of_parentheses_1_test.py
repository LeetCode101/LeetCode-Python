import unittest
from leetcode.algorithms.p0856_score_of_parentheses_1 import Solution


class TestScoreOfParentheses(unittest.TestCase):
    def test_score_of_parentheses(self):
        solution = Solution()

        self.assertEqual(1, solution.scoreOfParentheses('()'))
        self.assertEqual(2, solution.scoreOfParentheses('(())'))
        self.assertEqual(2, solution.scoreOfParentheses('()()'))
        self.assertEqual(6, solution.scoreOfParentheses('(()(()))'))
