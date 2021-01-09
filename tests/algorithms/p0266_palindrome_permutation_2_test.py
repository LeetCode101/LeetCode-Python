import unittest
from leetcode.algorithms.p0266_palindrome_permutation_2 import Solution


class TestPalindromePermutation(unittest.TestCase):
    def test_palindrome_permutation(self):
        solution = Solution()

        self.assertFalse(solution.canPermutePalindrome('code'))
        self.assertTrue(solution.canPermutePalindrome('carerac'))
