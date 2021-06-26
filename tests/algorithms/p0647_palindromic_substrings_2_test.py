import unittest
from leetcode.algorithms.p0647_palindromic_substrings_2 import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def test_palindromic_substrings(self):
        solution = Solution()

        self.assertEqual(3, solution.countSubstrings('abc'))
        self.assertEqual(6, solution.countSubstrings('aaa'))
