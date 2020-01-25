import unittest
from leetcode.algorithms.p0703_kth_largest_element_in_a_stream_1 \
    import KthLargest


class TestKthLargestElementInAStream(unittest.TestCase):
    def test_kth_largest_element_in_a_stream(self):
        kth_largest = KthLargest(3, [4, 5, 8, 2])

        self.assertEqual(4, kth_largest.add(3))
        self.assertEqual(5, kth_largest.add(5))
        self.assertEqual(5, kth_largest.add(10))
        self.assertEqual(8, kth_largest.add(9))
        self.assertEqual(8, kth_largest.add(4))
