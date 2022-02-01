import unittest
from leetcode.algorithms.p0994_rotting_oranges_2 import Solution


class TestRottingOranges(unittest.TestCase):
    def test_rotting_oranges(self):
        solution = Solution()

        self.assertEqual(-1, solution.orangesRotting(
            [[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
        self.assertEqual(4, solution.orangesRotting(
            [[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
        self.assertEqual(0, solution.orangesRotting([[0, 2]]))
