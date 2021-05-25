import unittest
from leetcode.algorithms.p0381_insert_delete_getrandom_o1_duplicates_allowed \
    import RandomizedCollection


class TestInsertDeleteGetRandomO1DuplicatesAllowed(unittest.TestCase):
    def test_insert_delete_getrandom_o1_duplicates_allowed(self):
        randomized_collection = RandomizedCollection()

        self.assertTrue(randomized_collection.insert(1))
        self.assertFalse(randomized_collection.insert(1))
        self.assertTrue(randomized_collection.insert(2))
        self.assertTrue(randomized_collection.getRandom() in [1, 2])
        self.assertTrue(randomized_collection.remove(1))
        self.assertFalse(randomized_collection.remove(3))
