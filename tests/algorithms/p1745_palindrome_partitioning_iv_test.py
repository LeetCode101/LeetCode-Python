import unittest
from leetcode.algorithms.p1745_palindrome_partitioning_iv import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        solution = Solution()

        self.assertTrue(solution.checkPartitioning('abcbdd'))
        self.assertFalse(solution.checkPartitioning('bcbddxy'))
