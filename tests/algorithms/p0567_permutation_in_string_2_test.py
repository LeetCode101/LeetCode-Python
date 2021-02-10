import unittest
from leetcode.algorithms.p0567_permutation_in_string_2 import Solution


class TestPermutationInString(unittest.TestCase):
    def test_permutation_in_string(self):
        solution = Solution()

        self.assertTrue(solution.checkInclusion('ab', 'eidbaooo'))
        self.assertFalse(solution.checkInclusion('ab', 'eidboaoo'))
        self.assertTrue(solution.checkInclusion('aba', 'eidbaaoo'))
