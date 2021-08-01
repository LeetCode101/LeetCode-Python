import unittest
from leetcode.algorithms.p1182_shortest_distance_to_target_color \
    import Solution


class TestShortestDistanceToTargetColor(unittest.TestCase):
    def test_shortest_distance_to_target_color(self):
        solution = Solution()

        self.assertListEqual([-1], solution.shortestDistanceColor(
            [1, 2], [[0, 3]]))
        self.assertListEqual([3, 0, 3], solution.shortestDistanceColor(
            [1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]))
        self.assertEqual([0, -1, -1, 1, 1], solution.shortestDistanceColor(
            [2, 1, 2, 2, 1], [[1, 1], [4, 3], [1, 3], [4, 2], [2, 1]]))
