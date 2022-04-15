import unittest
from leetcode.algorithms.p2116_check_if_a_parentheses_string_can_be_valid \
    import Solution


class TestCheckIfAParenthesesStringCanBeValid(unittest.TestCase):
    def test_check_if_a_parentheses_string_can_be_valid(self):
        solution = Solution()

        self.assertTrue(solution.canBeValid('))()))', '010100'))
        self.assertTrue(solution.canBeValid('()()', '0000'))
        self.assertFalse(solution.canBeValid(')', '0'))
        self.assertFalse(solution.canBeValid(
            '))))(())((()))))((()((((((())())((()))((((())()()))(()',
            '101100101111110000000101000101001010110001110000000101'))
        self.assertFalse(solution.canBeValid(
            '())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(',
            '100011110110011011010111100111011101111110000101001101001111'))
