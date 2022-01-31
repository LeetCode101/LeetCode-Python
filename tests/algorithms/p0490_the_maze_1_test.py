import unittest
from leetcode.algorithms.p0490_the_maze_1 import Solution


class TestTheMaze(unittest.TestCase):
    def test_the_maze(self):
        solution = Solution()

        self.assertTrue(solution.hasPath(
            [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [1, 2]))
        self.assertTrue(solution.hasPath(
            [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
        self.assertFalse(solution.hasPath(
            [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))
        self.assertFalse(solution.hasPath(
            [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]))
