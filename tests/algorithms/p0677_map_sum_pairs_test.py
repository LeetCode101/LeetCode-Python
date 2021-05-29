import unittest
from leetcode.algorithms.p0677_map_sum_pairs import MapSum


class TestMapSumPairs(unittest.TestCase):
    def test_map_sum_pairs(self):
        map_sum = MapSum()
        map_sum.insert('appled', 2)

        self.assertEqual(2, map_sum.sum('ap'))

        map_sum.insert('apple', 3)
        map_sum.insert('apple', 2)

        self.assertEqual(4, map_sum.sum('a'))
        self.assertEqual(0, map_sum.sum('aaa'))
