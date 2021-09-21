import unittest
from leetcode.algorithms.p1272_remove_interval_1 import Solution


class TestRemoveInterval(unittest.TestCase):
    def test_remove_interval(self):
        solution = Solution()

        self.assertListEqual([[50, 100]], solution.removeInterval(
            [[0, 100]], [0, 50]))
        self.assertListEqual([[0, 1], [6, 7]], solution.removeInterval(
            [[0, 2], [3, 4], [5, 7]], [1, 6]))
        self.assertListEqual([[0, 2], [3, 5]], solution.removeInterval(
            [[0, 5]], [2, 3]))
        self.assertListEqual(
            [[-5, -4], [-3, -2], [4, 5], [8, 9]], solution.removeInterval(
                [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]))
