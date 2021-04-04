import unittest
from leetcode.algorithms.p0145_binary_tree_postorder_traversal_2 \
    import Solution, TreeNode


class TestBinaryTreePostorderTraversal(unittest.TestCase):
    def test_binary_tree_postorder_traversal(self):
        solution = Solution()
        a = TreeNode(4)
        b = TreeNode(2, TreeNode(1), TreeNode(3))
        c = TreeNode(5)
        a.left = b
        a.right = c

        self.assertListEqual([], solution.postorderTraversal(None))
        self.assertListEqual([1, 3, 2, 5, 4], solution.postorderTraversal(a))
