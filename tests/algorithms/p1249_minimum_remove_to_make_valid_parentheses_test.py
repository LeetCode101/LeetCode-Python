import unittest
from leetcode.algorithms.p1249_minimum_remove_to_make_valid_parentheses \
    import Solution


class TestMinimumRemoveToMakeValidParentheses(unittest.TestCase):
    def test_minimum_remove_to_make_valid_parentheses(self):
        solution = Solution()

        self.assertTrue(solution.minRemoveToMakeValid('lee(t(c)o)de)') in
                        ['lee(t(c)o)de', 'lee(t(co)de)', 'lee(t(c)ode)'])
