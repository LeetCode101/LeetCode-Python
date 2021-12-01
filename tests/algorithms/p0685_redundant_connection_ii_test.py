import unittest
from leetcode.algorithms.p0685_redundant_connection_ii import Solution


class TestRedundantConnection(unittest.TestCase):
    def test_redundant_connection(self):
        solution = Solution()

        self.assertListEqual([2, 1], solution.findRedundantDirectedConnection(
            [[2, 1], [3, 1], [4, 2], [1, 4]]))
        self.assertListEqual([2, 3], solution.findRedundantDirectedConnection(
            [[1, 2], [1, 3], [2, 3]]))
        self.assertListEqual([4, 1], solution.findRedundantDirectedConnection(
            [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
