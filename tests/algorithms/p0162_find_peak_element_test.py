import unittest
from leetcode.algorithms.p0162_find_peak_element import Solution


class TestFindPeakElement(unittest.TestCase):
    def test_find_peak_element(self):
        solution = Solution()

        self.assertEqual(-1, solution.findPeakElement([]))
        self.assertEqual(2, solution.findPeakElement([1, 2, 3, 1]))
        self.assertEqual(1, solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
