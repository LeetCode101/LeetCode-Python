import unittest
from leetcode.algorithms.p0463_island_perimeter import Solution


class TestIslandPerimeter(unittest.TestCase):
    def test_island_perimeter(self):
        solution = Solution()

        self.assertEqual(0, solution.islandPerimeter([]))
        self.assertEqual(16, solution.islandPerimeter(
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
