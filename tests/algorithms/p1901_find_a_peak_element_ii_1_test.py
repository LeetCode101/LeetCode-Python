import unittest
from leetcode.algorithms.p1901_find_a_peak_element_ii_1 import Solution


class TestFindAPeakElement(unittest.TestCase):
    def test_find_a_peak_element(self):
        solution = Solution()

        self.assertListEqual([-1, -1], solution.findPeakGrid([[1, 1]]))
        self.assertListEqual([0, 1], solution.findPeakGrid([[1, 4], [3, 2]]))
        self.assertListEqual([1, 1], solution.findPeakGrid(
            [[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
