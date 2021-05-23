import unittest
from leetcode.algorithms.p0692_top_k_frequent_words_1 import Solution


class TestTopKFrequentWords(unittest.TestCase):
    def test_top_k_frequent_words(self):
        solution = Solution()

        self.assertListEqual(
            ['i'],
            solution.topKFrequent(['i', 'love', 'leetcode',
                                   'i', 'love', 'coding'], 1))
        self.assertListEqual(
            ['i', 'love'],
            solution.topKFrequent(['i', 'love', 'leetcode',
                                   'i', 'love', 'coding'], 2))
        self.assertListEqual(
            ['the', 'is', 'sunny', 'day'],
            solution.topKFrequent(['the', 'day', 'is', 'sunny', 'the', 'the',
                                   'the', 'sunny', 'is', 'is'], 4))
