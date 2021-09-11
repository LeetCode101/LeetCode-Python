import unittest
from leetcode.algorithms\
    .p0828_count_unique_characters_of_all_substrings_of_a_given_string_2 \
    import Solution


class TestCountUniqueCharactersOfAllSubstringsOfAGivenString(
        unittest.TestCase):
    def test_count_unique_characters_of_all_substrings_of_a_given_string(self):
        solution = Solution()

        self.assertEqual(10, solution.uniqueLetterString('ABC'))
        self.assertEqual(8, solution.uniqueLetterString('ABA'))
        self.assertEqual(92, solution.uniqueLetterString('LEETCODE'))
