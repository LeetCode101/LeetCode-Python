import unittest
from leetcode.algorithms.p0783_minimum_distance_between_bst_nodes_1 \
    import Solution, TreeNode


class TestMinimumDistanceBetweenBSTNodes(unittest.TestCase):
    def test_minimum_distance_between_bst_nodes(self):
        solution = Solution()
        root1 = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6)
        )

        self.assertEqual(0, solution.minDiffInBST(None))
        self.assertEqual(1, solution.minDiffInBST(root1))
