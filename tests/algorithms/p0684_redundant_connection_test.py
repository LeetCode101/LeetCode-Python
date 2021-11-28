import unittest
from leetcode.algorithms.p0684_redundant_connection import Solution


class TestRedundantConnection(unittest.TestCase):
    def test_redundant_connection(self):
        solution = Solution()

        self.assertListEqual([], solution.findRedundantConnection([]))
        self.assertListEqual([2, 3], solution.findRedundantConnection(
            [[1, 2], [1, 3], [2, 3]]))
        self.assertListEqual([1, 4], solution.findRedundantConnection(
            [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
