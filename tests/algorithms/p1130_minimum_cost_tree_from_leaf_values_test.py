import unittest
from leetcode.algorithms.p1130_minimum_cost_tree_from_leaf_values \
    import Solution


class TestMinimumCostTreeFromLeafValues(unittest.TestCase):
    def test_minimum_cost_tree_from_leaf_values(self):
        solution = Solution()

        self.assertEqual(32, solution.mctFromLeafValues([6, 2, 4]))
        self.assertEqual(44, solution.mctFromLeafValues([4, 11]))
        self.assertEqual(500, solution.mctFromLeafValues([15, 13, 5, 3, 15]))
