import unittest
from leetcode.algorithms.p0392_is_subsequence import Solution


class TestIsSubsequence(unittest.TestCase):
    def test_is_subsequence(self):
        solution = Solution()

        self.assertTrue(solution.isSubsequence('', 'a'))
        self.assertTrue(solution.isSubsequence('b', 'abc'))
        self.assertTrue(solution.isSubsequence('abc', 'ahbgdc'))
        self.assertFalse(solution.isSubsequence('axc', 'ahbgdc'))
