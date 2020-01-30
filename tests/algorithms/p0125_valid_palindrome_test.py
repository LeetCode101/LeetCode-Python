import unittest
from leetcode.algorithms.p0125_valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = Solution()

        self.assertTrue(
            solution.isPalindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(solution.isPalindrome('race a car'))
