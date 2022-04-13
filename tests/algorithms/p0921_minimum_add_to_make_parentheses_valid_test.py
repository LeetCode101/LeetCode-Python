import unittest
from leetcode.algorithms.p0921_minimum_add_to_make_parentheses_valid \
    import Solution


class TestMinimumAddToMakeParenthesesValid(unittest.TestCase):
    def test_minimum_add_to_make_parentheses_valid(self):
        solution = Solution()

        self.assertEqual(1, solution.minAddToMakeValid('())'))
        self.assertEqual(3, solution.minAddToMakeValid('((('))
