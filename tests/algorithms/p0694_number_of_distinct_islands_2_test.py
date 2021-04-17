import unittest
from leetcode.algorithms.p0694_number_of_distinct_islands_2 import Solution


class TestNumberOfDistinctIslands(unittest.TestCase):
    def test_number_of_distinct_islands(self):
        solution = Solution()

        self.assertEqual(0, solution.numDistinctIslands([]))
        self.assertEqual(3, solution.numDistinctIslands(
            [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))
