import unittest
from leetcode.algorithms.p0245_shortest_word_distance_iii import Solution


class TestShortestWordDistance(unittest.TestCase):
    def test_shortest_word_distance(self):
        solution = Solution()

        self.assertEqual(1, solution.shortestWordDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'],
            'makes', 'coding'))
        self.assertEqual(3, solution.shortestWordDistance(
            ['practice', 'makes', 'perfect', 'coding', 'makes'],
            'makes', 'makes'))
