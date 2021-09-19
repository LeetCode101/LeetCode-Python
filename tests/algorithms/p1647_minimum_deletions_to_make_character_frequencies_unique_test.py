import unittest
from leetcode.algorithms\
    .p1647_minimum_deletions_to_make_character_frequencies_unique \
    import Solution


class TestMinimumDeletionsToMakeCharacterFrequenciesUnique(unittest.TestCase):
    def test_minimum_deletions_to_make_character_frequencies_unique(self):
        solution = Solution()

        self.assertEqual(0, solution.minDeletions('aab'))
        self.assertEqual(2, solution.minDeletions('aaabbbcc'))
        self.assertEqual(2, solution.minDeletions('ceabaacb'))
