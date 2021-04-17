import unittest
from leetcode.algorithms.p0305_number_of_islands_ii_3 import Solution


class TestNumberOfIslands(unittest.TestCase):
    def test_number_of_islands(self):
        solution = Solution()

        self.assertListEqual([1, 1, 1, 1, 1], solution.numIslands2(
            5, 5, [[1, 1], [1, 2], [2, 1], [3, 1], [2, 2]]))
        self.assertListEqual([1, 1, 1, 1], solution.numIslands2(
            3, 3, [[0, 1], [0, 1], [0, 1], [0, 1]]))
        self.assertListEqual([1, 1, 2, 3], solution.numIslands2(
            3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
