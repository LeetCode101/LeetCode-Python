import unittest
from leetcode.algorithms.p0981_time_based_key_value_store import TimeMap


class TestTimeBasedKeyValueStore(unittest.TestCase):
    def test_time_based_key_value_store(self):
        time_map = TimeMap()
        time_map.set('foo', 'bar', 1)

        self.assertEqual('bar', time_map.get('foo', 1))
        self.assertEqual('bar', time_map.get('foo', 3))

        time_map.set('foo', 'bar2', 4)
        time_map.set('foo', 'bar3', 6)

        self.assertEqual('bar2', time_map.get('foo', 4))
        self.assertEqual('bar2', time_map.get('foo', 5))
