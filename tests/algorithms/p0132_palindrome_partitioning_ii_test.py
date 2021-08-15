import unittest
from leetcode.algorithms.p0132_palindrome_partitioning_ii import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        solution = Solution()

        self.assertEqual(1, solution.minCut('aab'))
        self.assertEqual(0, solution.minCut('a'))
