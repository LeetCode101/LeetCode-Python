import unittest
from leetcode.algorithms.p0417_pacific_atlantic_water_flow_2 import Solution


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def test_pacific_atlantic_water_flow(self):
        solution = Solution()

        self.assertListEqual([], solution.pacificAtlantic([]))
        self.assertListEqual(
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4],
                                      [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
                                      [5, 1, 1, 2, 4]]))
