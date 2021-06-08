import unittest
from leetcode.algorithms.p0107_binary_tree_level_order_traversal_ii_1 \
    import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def test_binary_tree_level_order_traversal(self):
        solution = Solution()
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )

        self.assertListEqual([[15, 7], [9, 20], [3]],
                             solution.levelOrderBottom(root))
