import unittest
from leetcode.algorithms.p1772_sort_features_by_popularity import Solution


class TestSortFeaturesByPopularity(unittest.TestCase):
    def test_sort_features_by_popularity(self):
        solution = Solution()

        self.assertListEqual(
            ['a', 'aa', 'b', 'c'], solution.sortFeatures(
                ['a', 'aa', 'b', 'c'], ['a', 'a aa', 'a a a a a', 'b a']))
        self.assertListEqual(
            ['touch', 'cooler', 'lock'], solution.sortFeatures(
                ['cooler', 'lock', 'touch'],
                ['i like cooler cooler', 'lock touch cool',
                 'locker like touch']))
