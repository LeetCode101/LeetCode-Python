import unittest
from leetcode.algorithms.p0131_palindrome_partitioning_1 import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        solution = Solution()

        self.assertListEqual([['a', 'a', 'b'], ['aa', 'b']],
                             solution.partition('aab'))
        self.assertListEqual([['a']], solution.partition('a'))
