import unittest
from leetcode.algorithms\
    .p0003_longest_substring_without_repeating_characters_2 import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_longest_substring_without_repeating_characters(self):
        solution = Solution()

        self.assertEqual(0, solution.lengthOfLongestSubstring(''))
        self.assertEqual(3, solution.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, solution.lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(3, solution.lengthOfLongestSubstring('pwwkew'))
