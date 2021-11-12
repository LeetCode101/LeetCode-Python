import unittest
from leetcode.algorithms.p1905_count_sub_islands_1 import Solution


class TestCountSubIslands(unittest.TestCase):
    def test_count_sub_islands(self):
        solution = Solution()
        grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
        grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]

        self.assertEqual(3, solution.countSubIslands(grid1, grid2))
