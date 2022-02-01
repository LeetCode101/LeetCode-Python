import unittest
from leetcode.algorithms.p0499_the_maze_iii import Solution


class TestTheMaze(unittest.TestCase):
    def test_the_maze(self):
        solution = Solution()

        self.assertEqual('u', solution.findShortestWay(
            [[0], [0]], [1, 0], [0, 0]))
        self.assertEqual('lul', solution.findShortestWay(
            [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [0, 1]))
        self.assertEqual('impossible', solution.findShortestWay(
            [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], [4, 3], [3, 0]))
        self.assertEqual('dldr', solution.findShortestWay(
            [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1]], [0, 4], [3, 5]))
