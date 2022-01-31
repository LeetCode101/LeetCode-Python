import unittest
from leetcode.algorithms.p0505_the_maze_ii import Solution


class TestTheMaze(unittest.TestCase):
    def test_the_maze(self):
        solution = Solution()

        self.assertEqual(12, solution.shortestDistance(
            [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
        self.assertEqual(-1, solution.shortestDistance(
            [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))
        self.assertEqual(-1, solution.shortestDistance(
            [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]))
