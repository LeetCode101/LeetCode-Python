import unittest
from leetcode.algorithms.p0451_sort_characters_by_frequency_2 import Solution


class TestSortCharactersByFrequency(unittest.TestCase):
    def test_sort_characters_by_frequency(self):
        solution = Solution()

        self.assertTrue(
            solution.frequencySort('tree') in ['eetr', 'eert'])
        self.assertTrue(
            solution.frequencySort('cccaaa') in ['aaaccc', 'cccaaa'])
        self.assertTrue(
            solution.frequencySort('Aabb') in ['bbAa', 'bbaA'])
