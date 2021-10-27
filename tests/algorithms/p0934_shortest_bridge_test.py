import unittest
from leetcode.algorithms.p0934_shortest_bridge import Solution


class TestShortestBridge(unittest.TestCase):
    def test_shortest_bridge(self):
        solution = Solution()

        self.assertEqual(1, solution.shortestBridge([[0, 1], [1, 0]]))
        self.assertEqual(2, solution.shortestBridge(
            [[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
        self.assertEqual(1, solution.shortestBridge(
            [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
