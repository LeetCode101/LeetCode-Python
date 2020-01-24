import unittest
from leetcode.algorithms.p0020_valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        solution = Solution()

        self.assertTrue(solution.isValid('()[]{}'))
        self.assertFalse(solution.isValid('([)]'))
        self.assertFalse(solution.isValid(']'))
