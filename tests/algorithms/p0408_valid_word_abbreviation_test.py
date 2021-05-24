import unittest
from leetcode.algorithms.p0408_valid_word_abbreviation import Solution


class TestValidWordAbbreviation(unittest.TestCase):
    def test_valid_word_abbreviation(self):
        solution = Solution()

        self.assertFalse(solution.validWordAbbreviation('a', '01'))
        self.assertFalse(solution.validWordAbbreviation('a', '2'))
        self.assertTrue(solution.validWordAbbreviation(
            'internationalization', 'i12iz4n'))
        self.assertFalse(solution.validWordAbbreviation('apple', 'a2e'))
