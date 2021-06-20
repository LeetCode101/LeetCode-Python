import unittest
from leetcode.algorithms.p0460_lfu_cache import LFUCache


class TestLFUCache(unittest.TestCase):
    def test_lfu_cache(self):
        lfu_cache = LFUCache(2)
        lfu_cache.put(1, 1)
        lfu_cache.put(2, 2)

        self.assertEqual(1, lfu_cache.get(1))

        lfu_cache.put(3, 3)

        self.assertEqual(-1, lfu_cache.get(2))
        self.assertEqual(3, lfu_cache.get(3))
