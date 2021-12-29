import unittest
from leetcode.algorithms.p1156_swap_for_longest_repeated_character_substring \
    import Solution


class TestSwapForLongestRepeatedCharacterSubstring(unittest.TestCase):
    def test_swap_for_longest_repeated_character_substring(self):
        solution = Solution()

        self.assertEqual(3, solution.maxRepOpt1('ababa'))
        self.assertEqual(6, solution.maxRepOpt1('aaabaaa'))
        self.assertEqual(5, solution.maxRepOpt1('aaaaa'))
