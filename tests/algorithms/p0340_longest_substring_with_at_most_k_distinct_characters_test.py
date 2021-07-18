import unittest
from leetcode.algorithms \
    .p0340_longest_substring_with_at_most_k_distinct_characters import Solution


class TestLongestSubstringWithAtMostKDistinctCharacters(unittest.TestCase):
    def test_longest_substring_with_at_most_k_distinct_characters(self):
        solution = Solution()

        self.assertEqual(4, solution.lengthOfLongestSubstringKDistinct(
            'abaccc', 2))
        self.assertEqual(3, solution.lengthOfLongestSubstringKDistinct(
            'bacc', 2))
        self.assertEqual(2, solution.lengthOfLongestSubstringKDistinct(
            'abee', 1))
        self.assertEqual(3, solution.lengthOfLongestSubstringKDistinct(
            'eceba', 2))
