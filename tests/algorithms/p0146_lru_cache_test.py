import unittest
from leetcode.algorithms.p0146_lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_lur_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)

        self.assertEqual(1, cache.get(1))

        cache.put(3, 3)

        self.assertEqual(-1, cache.get(2))

        cache.put(4, 4)
        cache.put(4, 5)

        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(5, cache.get(4))
