import unittest
from leetcode.algorithms\
    .p0159_longest_substring_with_at_most_two_distinct_characters \
    import Solution


class TestLongestSubstringWithAtMostTwoDistinctCharacters(unittest.TestCase):
    def test_longest_substring_with_at_most_two_distinct_characters(self):
        solution = Solution()

        self.assertEqual(3, solution.lengthOfLongestSubstringTwoDistinct(
            'eceba'))
