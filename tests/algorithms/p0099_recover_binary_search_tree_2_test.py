import unittest
from leetcode.algorithms.p0099_recover_binary_search_tree_2 \
    import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestRecoverBinarySearchTree(unittest.TestCase):
    def test_recover_binary_search_tree(self):
        solution = Solution()
        root1 = TreeNode(
            3,
            TreeNode(1),
            TreeNode(4, TreeNode(2))
        )
        root2 = TreeNode(
            1,
            TreeNode(3, None, TreeNode(2))
        )

        solution.recoverTree(root1)
        solution.recoverTree(root2)

        self.assertListEqual([1, 2, 3, 4], inorder(root1))
        self.assertListEqual([1, 2, 3], inorder(root2))
