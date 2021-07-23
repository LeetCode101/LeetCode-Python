import unittest
from leetcode.algorithms\
    .p1358_number_of_substrings_containing_all_three_characters_2 \
    import Solution


class TestNumberOfSubstringsContainingAllThreeCharacters(unittest.TestCase):
    def test_number_of_substrings_containing_all_three_characters(self):
        solution = Solution()

        self.assertEqual(10, solution.numberOfSubstrings('abcabc'))
