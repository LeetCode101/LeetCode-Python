import unittest
from leetcode.algorithms.p0295_find_median_from_data_stream_2 \
    import MedianFinder


class TestFindMedianFromDataStream(unittest.TestCase):
    def test_find_median_from_data_stream(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)

        self.assertEqual(1.5, median_finder.findMedian())

        median_finder.addNum(3)

        self.assertEqual(2, median_finder.findMedian())
