import unittest
from leetcode.algorithms.p1062_longest_repeating_substring_2 import Solution


class TestLongestRepeatingSubstring(unittest.TestCase):
    def test_longest_repeating_substring(self):
        solution = Solution()

        self.assertEqual(0, solution.longestRepeatingSubstring('abcd'))
        self.assertEqual(2, solution.longestRepeatingSubstring('abbaba'))
        self.assertEqual(3, solution.longestRepeatingSubstring('aabcaabdaab'))
        self.assertEqual(4, solution.longestRepeatingSubstring('aaaaa'))
