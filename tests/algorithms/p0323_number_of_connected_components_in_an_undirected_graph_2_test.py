import unittest
from leetcode.algorithms \
    .p0323_number_of_connected_components_in_an_undirected_graph_2 \
    import Solution


class TestNumberOfConnectedComponentsInAnUndirectedGraph(unittest.TestCase):
    def test_number_of_connected_components_in_an_undirected_graph(self):
        solution = Solution()

        self.assertEqual(2, solution.countComponents(
            4, [[2, 3], [1, 2], [1, 3]]))
        self.assertEqual(2, solution.countComponents(
            5, [[0, 1], [1, 2], [3, 4]]))
        self.assertEqual(1, solution.countComponents(
            5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
