import unittest
from leetcode.algorithms.p0779_k_th_symbol_in_grammar_2 import Solution


class TestKthSymbolInGrammar(unittest.TestCase):
    def test_k_th_symbol_in_grammar(self):
        solution = Solution()

        self.assertEqual(0, solution.kthGrammar(1, 1))
        self.assertEqual(0, solution.kthGrammar(2, 1))
        self.assertEqual(1, solution.kthGrammar(2, 2))
        self.assertEqual(0, solution.kthGrammar(3, 1))
        self.assertEqual(0, solution.kthGrammar(30, 434991989))
