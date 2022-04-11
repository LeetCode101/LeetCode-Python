import unittest
from leetcode.algorithms.p1087_brace_expansion import Solution


class TestBraceExpansion(unittest.TestCase):
    def test_brace_expansion(self):
        solution = Solution()

        self.assertListEqual(['acdf', 'acef', 'bcdf', 'bcef'],
                             solution.expand('{a,b}c{d,e}f'))
