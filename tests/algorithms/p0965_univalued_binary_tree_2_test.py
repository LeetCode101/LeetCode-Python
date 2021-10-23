import unittest
from leetcode.algorithms.p0965_univalued_binary_tree_2 \
    import Solution, TreeNode


class TestUnivaluedBinaryTree(unittest.TestCase):
    def test_univalued_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(1, TreeNode(1), TreeNode(1))
        )
        root2 = TreeNode(
            2,
            TreeNode(2, TreeNode(2), TreeNode(5))
        )

        self.assertTrue(solution.isUnivalTree(None))
        self.assertTrue(solution.isUnivalTree(root1))
        self.assertFalse(solution.isUnivalTree(root2))
