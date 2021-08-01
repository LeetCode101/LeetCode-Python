import unittest
from leetcode.algorithms.p1182_shortest_distance_to_target_color \
    import Solution


class TestShortestDistanceToTargetColor(unittest.TestCase):
    def test_shortest_distance_to_target_color(self):
        solution = Solution()

        self.assertListEqual([3, 0, 3], solution.shortestDistanceColor(
            [1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]))
