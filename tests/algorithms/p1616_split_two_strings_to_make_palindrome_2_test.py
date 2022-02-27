import unittest
from leetcode.algorithms.p1616_split_two_strings_to_make_palindrome_2 \
    import Solution


class TestSplitTwoStringsToMakePalindrome(unittest.TestCase):
    def test_split_two_strings_to_make_palindrome(self):
        solution = Solution()

        self.assertTrue(solution.checkPalindromeFormation('x', 'y'))
        self.assertFalse(solution.checkPalindromeFormation('xbdef', 'xecab'))
        self.assertTrue(solution.checkPalindromeFormation('ulacfd', 'jizalu'))
        self.assertTrue(solution.checkPalindromeFormation(
            'pvhmupgqeltozftlmfjjde', 'yjgpzbezspnnpszebzmhvp'))
