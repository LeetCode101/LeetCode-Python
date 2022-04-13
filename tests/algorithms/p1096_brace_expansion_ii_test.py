import unittest
from leetcode.algorithms.p1096_brace_expansion_ii import Solution


class TestBraceExpansion(unittest.TestCase):
    def test_brace_expansion(self):
        solution = Solution()

        self.assertListEqual(['ac', 'ad', 'ae', 'bc', 'bd', 'be'],
                             solution.braceExpansionII('{a,b}{c,{d,e}}'))
        self.assertListEqual(['a', 'ab', 'ac', 'z'],
                             solution.braceExpansionII(
                                 '{{a,z},a{b,c},{ab,z}}'))
