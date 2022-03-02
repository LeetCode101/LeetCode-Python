import unittest
from leetcode.algorithms.p0524_longest_word_in_dictionary_through_deleting_1 \
    import Solution


class TestLongestWordInDictionaryThroughDeleting(unittest.TestCase):
    def test_longest_word_in_dictionary_through_deleting(self):
        solution = Solution()

        self.assertEqual('apple', solution.findLongestWord(
            'abpcplea', ['ale', 'apple', 'monkey', 'plea']))
        self.assertEqual('a', solution.findLongestWord(
            'abpcplea', ['a', 'b', 'c']))
        self.assertEqual('abc', solution.findLongestWord(
            'abce', ['abe', 'abc']))
