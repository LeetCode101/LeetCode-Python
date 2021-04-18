import unittest
from leetcode.algorithms.p1254_number_of_closed_islands_2 import Solution


class TestNumberOfClosedIslands(unittest.TestCase):
    def test_number_of_closed_islands(self):
        solution = Solution()

        self.assertEqual(0, solution.closedIsland([]))
        self.assertEqual(2, solution.closedIsland(
            [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0],
             [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 0]]))
        self.assertEqual(1, solution.closedIsland(
            [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
        self.assertEqual(2, solution.closedIsland(
            [[1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1]]))
