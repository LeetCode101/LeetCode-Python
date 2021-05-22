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

        self.assertFalse(hash_set.contains(15))
        self.assertTrue(hash_set.contains(1))
        self.assertTrue(hash_set.contains(34))

        hash_set.remove(1)
        hash_set.remove(16)
        hash_set.remove(32)
        hash_set.add(32)
        hash_set.add(16)
        hash_set.add(64)
        hash_set.add(48)
        hash_set.remove(32)

        for i in range(100):
            hash_set.add(i)
