import unittest
from leetcode.algorithms.p0094_binary_tree_inorder_traversal_2 \
    import Solution, TreeNode


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def test_binary_tree_inorder_traversal(self):
        solution = Solution()
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)
        a.right = b
        b.left = c

        self.assertListEqual([1, 3, 2], solution.inorderTraversal(a))
