import unittest
from leetcode.algorithms.p1278_palindrome_partitioning_iii import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        solution = Solution()

        self.assertEqual(1, solution.palindromePartition('abc', 2))
        self.assertEqual(0, solution.palindromePartition('aabbc', 3))
        self.assertEqual(0, solution.palindromePartition('leetcode', 8))
        self.assertEqual(6, solution.palindromePartition(
            'spsvmwkvwyfnrrfklevvyxsayc', 6))
