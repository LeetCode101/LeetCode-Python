import unittest
from leetcode.algorithms.p0243_shortest_word_distance import Solution


class TestShortestWordDistance(unittest.TestCase):
    def test_shortest_word_distance(self):
        solution = Solution()

        self.assertEqual(3, solution.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'],
            'coding', 'practice'))
        self.assertEqual(1, solution.shortestDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'],
            'makes', 'coding'))
