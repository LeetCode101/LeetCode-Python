import unittest
from leetcode.algorithms.p0314_binary_tree_vertical_order_traversal \
    import Solution, TreeNode


class TestBinaryTreeVerticalOrderTraversal(unittest.TestCase):
    def test_binary_tree_vertical_order_traversal(self):
        solution = Solution()
        root = TreeNode(
            3,
            TreeNode(9, TreeNode(4), TreeNode(0)),
            TreeNode(8, TreeNode(1), TreeNode(7))
        )

        self.assertListEqual([[4], [9], [3, 0, 1], [8], [7]],
                             solution.verticalOrder(root))
