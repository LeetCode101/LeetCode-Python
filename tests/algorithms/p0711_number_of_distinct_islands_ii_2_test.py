import unittest
from leetcode.algorithms.p0711_number_of_distinct_islands_ii_2 import Solution


class TestNumberOfDistinctIslands(unittest.TestCase):
    def test_number_of_distinct_islands(self):
        solution = Solution()

        self.assertEqual(0, solution.numDistinctIslands2([]))
        self.assertEqual(1, solution.numDistinctIslands2(
            [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]))
        self.assertEqual(2, solution.numDistinctIslands2(
            [[1, 1, 1, 0, 0], [1, 0, 0, 0, 1],
             [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]))
