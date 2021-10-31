import unittest
from leetcode.algorithms.p0865_smallest_subtree_with_all_the_deepest_nodes \
    import Solution, TreeNode


class TestSmallestSubtreeWithAllTheDeepestNodes(unittest.TestCase):
    def test_smallest_subtree_with_all_the_deepest_nodes(self):
        solution = Solution()
        a = TreeNode(2, TreeNode(7), TreeNode(4))
        root1 = TreeNode(
            3,
            TreeNode(5, TreeNode(6), a),
            TreeNode(1, TreeNode(0), TreeNode(8))
        )
        root2 = TreeNode(1)

        self.assertEqual(a, solution.subtreeWithAllDeepest(root1))
        self.assertEqual(root2, solution.subtreeWithAllDeepest(root2))
