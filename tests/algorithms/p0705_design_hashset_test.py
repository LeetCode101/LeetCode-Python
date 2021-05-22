import unittest
from leetcode.algorithms.p0705_design_hashset import MyHashSet


class TestDesignHashSet(unittest.TestCase):
    def test_design_hashset(self):
        hash_set = MyHashSet()
        hash_set.add(1)
        hash_set.add(2)

        self.assertTrue(hash_set.contains(1))

        hash_set.remove(1)

        self.assertFalse(hash_set.contains(1))

        for i in range(100):
            hash_set.add(i)

        for i in range(100):
            self.assertTrue(hash_set.contains(i))
