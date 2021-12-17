import unittest
from leetcode.algorithms.p0261_graph_valid_tree_1 import Solution


class TestGraphValidTree(unittest.TestCase):
    def test_graph_valid_tree(self):
        solution = Solution()

        self.assertTrue(solution.validTree(
            5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertFalse(solution.validTree(
            5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
