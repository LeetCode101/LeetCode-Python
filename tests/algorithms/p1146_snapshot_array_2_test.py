import unittest
from leetcode.algorithms.p1146_snapshot_array_2 import SnapshotArray


class TestSnapshotArray(unittest.TestCase):
    def test_snapshot_array(self):
        snapshot_array = SnapshotArray(3)
        snapshot_array.set(0, 5)
        snapshot_array.set(0, 4)

        self.assertEqual(0, snapshot_array.snap())

        snapshot_array.set(0, 6)

        self.assertEqual(4, snapshot_array.get(0, 0))
