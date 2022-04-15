import unittest
from leetcode.algorithms.p2116_check_if_a_parentheses_string_can_be_valid \
    import Solution


class TestCheckIfAParenthesesStringCanBeValid(unittest.TestCase):
    def test_check_if_a_parentheses_string_can_be_valid(self):
        solution = Solution()

        self.assertTrue(solution.canBeValid('))()))', '010100'))
        self.assertTrue(solution.canBeValid('()()', '0000'))
        self.assertFalse(solution.canBeValid(')', '0'))
