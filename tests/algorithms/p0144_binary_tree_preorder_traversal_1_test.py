import unittest
from leetcode.algorithms.p0144_binary_tree_preorder_traversal_1 \
    import Solution, TreeNode


class TestBinaryTreePreorderTraversal(unittest.TestCase):
    def test_binary_tree_preorder_traversal(self):
        solution = Solution()
        a = TreeNode(4)
        b = TreeNode(2, TreeNode(1), TreeNode(3))
        c = TreeNode(5)
        a.left = b
        a.right = c

        self.assertListEqual([], solution.preorderTraversal(None))
        self.assertListEqual([4, 2, 1, 3, 5], solution.preorderTraversal(a))
