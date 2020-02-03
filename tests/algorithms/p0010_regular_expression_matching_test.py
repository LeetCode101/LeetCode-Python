import unittest
from leetcode.algorithms.p0010_regular_expression_matching import Solution


class TestRegularExpressionMatching(unittest.TestCase):
    def test_regular_expression_matching(self):
        solution = Solution()

        self.assertFalse(solution.isMatch('aa', 'a'))
        self.assertFalse(solution.isMatch('aa', '*'))
        self.assertTrue(solution.isMatch('ab', '.*'))
        self.assertTrue(solution.isMatch('aab', 'c*a*b'))
        self.assertFalse(solution.isMatch('mississippi', 'mis*is*p*.'))
