import unittest
from leetcode.algorithms.p1971_find_if_path_exists_in_graph_3 import Solution


class TestFindIfPathExistsInGraph(unittest.TestCase):
    def test_find_if_path_exists_in_graph(self):
        solution = Solution()

        self.assertTrue(solution.validPath(
            3, [[0, 1], [1, 2], [2, 0]], 0, 2))
        self.assertFalse(solution.validPath(
            6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
