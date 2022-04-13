import unittest
from leetcode.algorithms\
    .p1750_minimum_length_of_string_after_deleting_similar_ends import Solution


class TestMinimumLengthOfStringAfterDeletingSimilarEnds(unittest.TestCase):
    def test_minimum_length_of_string_after_deleting_similar_ends(self):
        solution = Solution()

        self.assertEqual(0, solution.minimumLength(''))
        self.assertEqual(1, solution.minimumLength(
            'bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb'))
        self.assertEqual(2, solution.minimumLength('ca'))
        self.assertEqual(0, solution.minimumLength('cabaabac'))
        self.assertEqual(3, solution.minimumLength('aabccabba'))
