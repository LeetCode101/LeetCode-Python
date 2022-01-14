import unittest
from leetcode.algorithms.p1081_smallest_subsequence_of_distinct_characters \
    import Solution


class TestSmallestSubsequenceOfDistinctCharacters(unittest.TestCase):
    def test_smallest_subsequence_of_distinct_characters(self):
        solution = Solution()

        self.assertEqual('abc', solution.smallestSubsequence(
            'cbaacabcaaccaacababa'))
        self.assertEqual('abc', solution.smallestSubsequence('bcabc'))
        self.assertEqual('acdb', solution.smallestSubsequence('cbacdcbc'))
