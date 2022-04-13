import unittest
from leetcode.algorithms\
    .p1541_minimum_insertions_to_balance_a_parentheses_string import Solution


class TestMinimumInsertionsToBalanceAParenthesesString(unittest.TestCase):
    def test_minimum_insertions_to_balance_a_parentheses_string(self):
        solution = Solution()

        self.assertEqual(3, solution.minInsertions('))())('))
        self.assertEqual(1, solution.minInsertions('(()))'))
        self.assertEqual(0, solution.minInsertions('())'))
