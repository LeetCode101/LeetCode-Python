import unittest
from leetcode.algorithms.p0845_longest_mountain_in_array import Solution


class TestLongestMountainInArray(unittest.TestCase):
    def test_longest_mountain_in_array(self):
        solution = Solution()

        self.assertEqual(0, solution.longestMountain(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(0, solution.longestMountain([2, 2, 2]))
        self.assertEqual(5, solution.longestMountain([2, 1, 4, 7, 3, 2, 5]))
