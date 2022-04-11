import unittest
from leetcode.algorithms.p2101_detonate_the_maximum_bombs_2 import Solution


class TestDetonateTheMaximumBombs(unittest.TestCase):
    def test_detonate_the_maximum_bombs(self):
        solution = Solution()

        self.assertEqual(2, solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]))
        self.assertEqual(1, solution.maximumDetonation(
            [[1, 1, 5], [10, 10, 5]]))
        self.assertEqual(5, solution.maximumDetonation(
            [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
