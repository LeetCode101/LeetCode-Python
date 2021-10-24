import unittest
from leetcode.algorithms.p0310_minimum_height_trees_2 import Solution


class TestMinimumHeightTrees(unittest.TestCase):
    def test_minimum_height_trees(self):
        solution = Solution()

        self.assertListEqual([0], solution.findMinHeightTrees(1, []))
        self.assertListEqual([1], solution.findMinHeightTrees(
            4, [[1, 0], [1, 2], [1, 3]]))
        self.assertListEqual([3, 4], solution.findMinHeightTrees(
            6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
