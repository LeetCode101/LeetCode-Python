import unittest
from leetcode.algorithms.p0044_wildcard_matching import Solution


class TestWildcardMatching(unittest.TestCase):
    def test_wildcard_matching(self):
        solution = Solution()

        self.assertFalse(solution.isMatch('aa', 'a'))
        self.assertTrue(solution.isMatch('aa', '*'))
        self.assertFalse(solution.isMatch('cb', '?a'))
        self.assertTrue(solution.isMatch('adceb', '*a*b'))
        self.assertFalse(solution.isMatch('acdcb', 'a*c?b'))
