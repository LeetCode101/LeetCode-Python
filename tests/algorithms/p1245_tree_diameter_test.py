import unittest
from leetcode.algorithms.p1245_tree_diameter import Solution


class TestTreeDiameter(unittest.TestCase):
    def test_tree_diameter(self):
        solution = Solution()

        self.assertEqual(0, solution.treeDiameter([]))
        self.assertEqual(4, solution.treeDiameter(
            [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
