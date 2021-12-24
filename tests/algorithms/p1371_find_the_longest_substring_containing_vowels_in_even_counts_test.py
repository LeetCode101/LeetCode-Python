import unittest
from leetcode.algorithms\
    .p1371_find_the_longest_substring_containing_vowels_in_even_counts \
    import Solution


class TestFindTheLongestSubstringContainingVowelsInEvenCounts(
        unittest.TestCase):
    def test_find_the_longest_substring_containing_vowels_in_even_counts(self):
        solution = Solution()

        self.assertEqual(13, solution.findTheLongestSubstring(
            'eleetminicoworoep'))
        self.assertEqual(5, solution.findTheLongestSubstring(
            'leetcodeisgreat'))
        self.assertEqual(6, solution.findTheLongestSubstring('bcbcbc'))
