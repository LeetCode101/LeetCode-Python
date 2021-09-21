import unittest
from leetcode.algorithms.p0436_find_right_interval import Solution


class TestFindRightInterval(unittest.TestCase):
    def test_find_right_interval(self):
        solution = Solution()

        self.assertListEqual([0, -1], solution.findRightInterval(
            [[1, 1], [3, 4]]))
        self.assertListEqual([-1, 0, 1], solution.findRightInterval(
            [[4, 5], [2, 3], [1, 2]]))
        self.assertListEqual([-1], solution.findRightInterval([[1, 2]]))
        self.assertListEqual([-1, 0, 1], solution.findRightInterval(
            [[3, 4], [2, 3], [1, 2]]))
        self.assertListEqual([-1, 2, -1], solution.findRightInterval(
            [[1, 4], [2, 3], [3, 4]]))
