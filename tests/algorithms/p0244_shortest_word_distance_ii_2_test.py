import unittest
from leetcode.algorithms.p0244_shortest_word_distance_ii_2 import WordDistance


class TestShortestWordDistance(unittest.TestCase):
    def test_shortest_word_distance(self):
        word_distance = WordDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'])

        self.assertEqual(3, word_distance.shortest('coding', 'practice'))
        self.assertEqual(1, word_distance.shortest('makes', 'coding'))
