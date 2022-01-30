import unittest
from leetcode.algorithms.p1631_path_with_minimum_effort_1 import Solution


class TestPathWithMinimumEffort(unittest.TestCase):
    def test_path_with_minimum_effort(self):
        solution = Solution()

        self.assertEqual(2, solution.minimumEffortPath(
            [[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
        self.assertEqual(1, solution.minimumEffortPath(
            [[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
