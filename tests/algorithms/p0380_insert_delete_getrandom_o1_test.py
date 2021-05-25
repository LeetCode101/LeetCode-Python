import unittest
from leetcode.algorithms.p0380_insert_delete_getrandom_o1 import RandomizedSet


class TestInsertDeleteGetRandomO1(unittest.TestCase):
    def test_insert_delete_getrandom_o1(self):
        randomized_set = RandomizedSet()

        self.assertTrue(randomized_set.insert(1))
        self.assertFalse(randomized_set.remove(2))
        self.assertTrue(randomized_set.insert(2))
        self.assertTrue(randomized_set.getRandom() in [1, 2])
        self.assertTrue(randomized_set.remove(1))
        self.assertFalse(randomized_set.insert(2))
