import unittest
from leetcode.algorithms.p0208_implement_trie_2 import Trie


class TestImplementTrie(unittest.TestCase):
    def test_implement_trie(self):
        trie = Trie()
        trie.insert('apple')

        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))

        trie.insert('app')

        self.assertTrue(trie.search('app'))
        self.assertFalse(trie.search('cat'))
        self.assertFalse(trie.startsWith('dog'))
