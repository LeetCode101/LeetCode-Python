import unittest
from leetcode.algorithms.p0062_unique_paths_1 import Solution


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths(self):
        solution = Solution()

        self.assertEqual(28, solution.uniquePaths(3, 7))
