import unittest
from leetcode.algorithms.p1383_maximum_performance_of_a_team import Solution


class TestMaximumPerformanceOfATeam(unittest.TestCase):
    def test_maximum_performance_of_a_team(self):
        solution = Solution()

        self.assertEqual(60, solution.maxPerformance(
            6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
        self.assertEqual(68, solution.maxPerformance(
            6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3))
        self.assertEqual(72, solution.maxPerformance(
            6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4))
