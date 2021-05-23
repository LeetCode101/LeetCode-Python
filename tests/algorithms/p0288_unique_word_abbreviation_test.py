import unittest
from leetcode.algorithms.p0288_unique_word_abbreviation import ValidWordAbbr


class TestUniqueWordAbbreviation(unittest.TestCase):
    def test_unique_word_abbreviation(self):
        abbr = ValidWordAbbr(['deer', 'door', 'cake', 'card', 'it'])

        self.assertFalse(abbr.isUnique('dear'))
        self.assertTrue(abbr.isUnique('cart'))
        self.assertFalse(abbr.isUnique('cane'))
        self.assertTrue(abbr.isUnique('make'))
        self.assertTrue(abbr.isUnique('cake'))
