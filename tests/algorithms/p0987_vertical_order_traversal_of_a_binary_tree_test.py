import unittest
from leetcode.algorithms.p0987_vertical_order_traversal_of_a_binary_tree \
    import Solution, TreeNode


class TestVerticalOrderTraversalOfABinaryTree(unittest.TestCase):
    def test_vertical_order_traversal_of_a_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6), TreeNode(7))
        )

        self.assertListEqual([[4], [2], [1, 5, 6], [3], [7]],
                             solution.verticalTraversal(root))
