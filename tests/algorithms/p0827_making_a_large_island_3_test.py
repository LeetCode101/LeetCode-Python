import unittest
from leetcode.algorithms.p0827_making_a_large_island_3 import Solution


class TestMakingALargeIsland(unittest.TestCase):
    def test_making_a_large_island(self):
        solution = Solution()

        self.assertEqual(0, solution.largestIsland([]))
        self.assertEqual(3, solution.largestIsland([[1, 0], [0, 1]]))
        self.assertEqual(4, solution.largestIsland([[1, 1], [1, 0]]))
        self.assertEqual(4, solution.largestIsland([[1, 1], [1, 1]]))
