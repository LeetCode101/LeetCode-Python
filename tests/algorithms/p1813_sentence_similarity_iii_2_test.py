import unittest
from leetcode.algorithms.p1813_sentence_similarity_iii_2 import Solution


class TestSentenceSimilarity(unittest.TestCase):
    def test_sentence_similarity(self):
        solution = Solution()

        self.assertTrue(solution.areSentencesSimilar(
            'My name is Haley', 'My Haley'))
        self.assertFalse(solution.areSentencesSimilar('of', 'A lot of words'))
        self.assertTrue(solution.areSentencesSimilar(
            'Eating right now', 'Eating'))
        self.assertFalse(solution.areSentencesSimilar('Luky', 'Lucccky'))
