import unittest
from leetcode.algorithms.p0022_generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def test_generate_parentheses(self):
        solution = Solution()
        expected_lists = [
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()'
        ]

        self.assertListEqual(expected_lists, solution.generateParenthesis(3))
