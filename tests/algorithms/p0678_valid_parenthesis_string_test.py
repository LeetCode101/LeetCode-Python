import unittest
from leetcode.algorithms.p0678_valid_parenthesis_string import Solution


class TestValidParenthesisString(unittest.TestCase):
    def test_valid_parenthesis_string(self):
        solution = Solution()

        self.assertTrue(solution.checkValidString('()'))
        self.assertTrue(solution.checkValidString('(*)'))
        self.assertTrue(solution.checkValidString('(*))'))
        self.assertFalse(solution.checkValidString(')'))
        self.assertTrue(solution.checkValidString('(*'))
        self.assertFalse(solution.checkValidString('*('))
