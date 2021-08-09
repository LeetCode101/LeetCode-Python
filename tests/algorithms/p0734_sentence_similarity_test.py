import unittest
from leetcode.algorithms.p0734_sentence_similarity import Solution


class TestSentenceSimilarity(unittest.TestCase):
    def test_sentence_similarity(self):
        solution = Solution()

        self.assertTrue(solution.areSentencesSimilar(
            ['a'], ['b'], [['a', 'b']]))
        self.assertFalse(solution.areSentencesSimilar(['a'], ['b'], []))
        self.assertFalse(solution.areSentencesSimilar(['a'], ['a', 'b'], []))
        self.assertTrue(solution.areSentencesSimilar(
            ['great', 'acting', 'skills'], ['fine', 'drama', 'talent'],
            [['great', 'fine'], ['drama', 'acting'], ['skills', 'talent']]))
