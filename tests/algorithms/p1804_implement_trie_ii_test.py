import unittest
from leetcode.algorithms.p1804_implement_trie_ii import Trie


class TestImplementTrie(unittest.TestCase):
    def test_implement_trie(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')

        self.assertEqual(2, trie.countWordsEqualTo('apple'))
        self.assertEqual(2, trie.countWordsStartingWith('app'))

        trie.erase('apple')

        self.assertEqual(1, trie.countWordsEqualTo('apple'))
        self.assertEqual(1, trie.countWordsStartingWith('app'))

        trie.erase('apple')
        trie.erase('abc')

        self.assertEqual(0, trie.countWordsEqualTo('apple'))
        self.assertEqual(0, trie.countWordsStartingWith('app'))
