import unittest
from leetcode.algorithms.p0737_sentence_similarity_ii import Solution


class TestSentenceSimilarity(unittest.TestCase):
    def test_sentence_similarity(self):
        solution = Solution()

        self.assertFalse(solution.areSentencesSimilarTwo(
            ['a'], ['a', 'b'], []))
        self.assertTrue(solution.areSentencesSimilarTwo(
            ['great', 'acting', 'skills'], ['fine', 'drama', 'talent'],
            [['great', 'good'], ['fine', 'good'], ['drama', 'acting'],
             ['skills', 'talent']]))
        self.assertTrue(solution.areSentencesSimilarTwo(
            ['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'],
            [['manga', 'onepiece'], ['platform', 'anime'],
             ['leetcode', 'platform'], ['anime', 'manga']]))
        self.assertFalse(solution.areSentencesSimilarTwo(
            ['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'],
            [['manga', 'hunterXhunter'], ['platform', 'anime'],
             ['leetcode', 'platform'], ['anime', 'manga']]))
