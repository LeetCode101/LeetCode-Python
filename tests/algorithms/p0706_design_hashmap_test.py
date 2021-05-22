import unittest
from leetcode.algorithms.p0706_design_hashmap import MyHashMap


class TestDesignHashMap(unittest.TestCase):
    def test_design_hashmap(self):
        hash_map = MyHashMap()

        for i in range(16, 19):
            hash_map.put(i, i)

        for i in range(3):
            hash_map.put(i, i)

        for i in range(32, 35):
            hash_map.put(i, i)

        self.assertEqual(-1, hash_map.get(15))
        self.assertEqual(1, hash_map.get(1))
        self.assertEqual(34, hash_map.get(34))

        hash_map.remove(1)
        hash_map.remove(16)
        hash_map.remove(32)
        hash_map.put(32, 32)
        hash_map.put(16, 16)
        hash_map.put(64, 64)
        hash_map.put(48, 48)
        hash_map.remove(32)

        for i in range(100):
            hash_map.put(i, i)
