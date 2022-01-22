import unittest
from leetcode.algorithms.p1901_find_a_peak_element_ii_2 import Solution


class TestFindAPeakElement(unittest.TestCase):
    def test_find_a_peak_element(self):
        solution = Solution()
        grid = [
            [55, 77, 9, 50, 49, 77, 60, 68, 33, 71, 2, 88, 93, 15, 88, 69,
             97, 35, 99, 83, 44, 15, 38],
            [56, 21, 59, 1, 93, 34, 65, 98, 23, 65, 14, 81, 39, 82, 65, 78,
             26, 20, 48, 98, 21, 70, 100],
            [68, 1, 77, 42, 63, 3, 15, 47, 40, 31, 8, 31, 73, 11, 94, 63, 9,
             98, 69, 99, 17, 85, 61],
            [71, 22, 34, 68, 78, 55, 28, 70, 97, 94, 89, 26, 92, 40, 52, 86,
             84, 48, 57, 67, 58, 16, 32],
            [29, 9, 44, 3, 76, 71, 30, 76, 29, 1, 10, 91, 81, 8, 30, 9, 5,
             43, 10, 66, 31, 36, 86],
            [63, 28, 70, 17, 93, 74, 61, 32, 61, 53, 25, 13, 85, 56, 46, 55,
             53, 60, 94, 7, 87, 84, 83],
            [13, 8, 52, 94, 44, 14, 32, 25, 69, 58, 18, 55, 24, 36, 60, 32,
             10, 57, 71, 13, 7, 70, 2]]

        self.assertListEqual([-1, -1], solution.findPeakGrid([[1, 1]]))
        self.assertListEqual([0, 1], solution.findPeakGrid([[1, 4], [3, 2]]))
        self.assertListEqual([1, 1], solution.findPeakGrid(
            [[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
        self.assertListEqual([4, 11], solution.findPeakGrid(grid))
