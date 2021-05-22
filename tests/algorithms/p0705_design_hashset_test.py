import unittest
from leetcode.algorithms.p0705_design_hashset import MyHashSet


class TestDesignHashSet(unittest.TestCase):
    def test_design_hashset(self):
        hash_set = MyHashSet()

        for i in range(16, 19):
            hash_set.add(i)

        for i in range(3):
            hash_set.add(i)

        for i in range(32, 35):
            hash_set.add(i)

        self.assertTrue(hash_set.contains(16))

        hash_set.remove(16)
        hash_set.remove(1)

        self.assertFalse(hash_set.contains(16))
        self.assertFalse(hash_set.contains(1))
