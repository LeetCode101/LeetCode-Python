import unittest
from leetcode.algorithms.p1557_minimum_number_of_vertices_to_reach_all_nodes \
    import Solution


class TestMinimumNumberOfVerticesToReachAllNodes(unittest.TestCase):
    def test_minimum_number_of_vertices_to_reach_all_nodes(self):
        solution = Solution()

        self.assertListEqual([0, 3], sorted(
            solution.findSmallestSetOfVertices(
                6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])))
        self.assertListEqual([0, 2, 3], sorted(
            solution.findSmallestSetOfVertices(
                5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]])))
