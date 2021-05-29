import unittest
from leetcode.algorithms.p0211_design_add_and_search_words_data_structure \
    import WordDictionary


class TestDesignAddAndSearchWordsDataStructure(unittest.TestCase):
    def test_design_add_and_search_words_data_structure(self):
        word_dictionary = WordDictionary()
        word_dictionary.addWord('bad')
        word_dictionary.addWord('dad')
        word_dictionary.addWord('mad')

        self.assertFalse(word_dictionary.search('pad'))
        self.assertTrue(word_dictionary.search('bad'))
        self.assertTrue(word_dictionary.search('.ad'))
        self.assertTrue(word_dictionary.search('b..'))
        self.assertFalse(word_dictionary.search('b...'))
