import unittest
from leetcode.algorithms.p0852_peak_index_in_a_mountain_array_2 import Solution


class TestPeakIndexInAMountainArray(unittest.TestCase):
    def test_peak_index_in_a_mountain_array(self):
        solution = Solution()

        self.assertEqual(1, solution.peakIndexInMountainArray([0, 1, 0]))
        self.assertEqual(1, solution.peakIndexInMountainArray([0, 2, 1, 0]))
        self.assertEqual(1, solution.peakIndexInMountainArray([0, 10, 5, 2]))
        self.assertEqual(2, solution.peakIndexInMountainArray([3, 4, 5, 1]))
        self.assertEqual(2, solution.peakIndexInMountainArray(
            [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
