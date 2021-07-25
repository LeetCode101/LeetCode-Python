import unittest
from leetcode.algorithms.p0424_longest_repeating_character_replacement_2 \
    import Solution


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def test_longest_repeating_character_replacement(self):
        solution = Solution()

        self.assertEqual(4, solution.characterReplacement('ABAB', 2))
        self.assertEqual(4, solution.characterReplacement('AABABBA', 1))
