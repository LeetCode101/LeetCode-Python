import unittest
from leetcode.algorithms.p0433_minimum_genetic_mutation import Solution


class TestMinimumGeneticMutation(unittest.TestCase):
    def test_minimum_genetic_mutation(self):
        solution = Solution()

        self.assertEqual(-1, solution.minMutation(
            'AACCGGTT', 'AACCGGTA', []))
        self.assertEqual(1, solution.minMutation(
            'AACCGGTT', 'AACCGGTA', ['AACCGGTA']))
        self.assertEqual(2, solution.minMutation(
            'AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']))
        self.assertEqual(3, solution.minMutation(
            'AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC']))
