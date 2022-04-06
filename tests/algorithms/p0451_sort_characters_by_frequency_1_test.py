import unittest
from leetcode.algorithms.p0451_sort_characters_by_frequency_1 import Solution


class TestSortCharactersByFrequency(unittest.TestCase):
    def test_sort_characters_by_frequency(self):
        solution = Solution()

        self.assertEqual('eert', solution.frequencySort('tree'))
        self.assertEqual('aaaccc', solution.frequencySort('cccaaa'))
        self.assertEqual('bbAa', solution.frequencySort('Aabb'))
