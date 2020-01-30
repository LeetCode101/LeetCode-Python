import unittest
from leetcode.algorithms.p0072_edit_distance import Solution


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        solution = Solution()

        self.assertEqual(3, solution.minDistance('horse', 'ros'))
        self.assertEqual(5, solution.minDistance('intention', 'execution'))
