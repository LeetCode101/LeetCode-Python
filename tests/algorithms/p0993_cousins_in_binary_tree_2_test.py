import unittest
from leetcode.algorithms.p0993_cousins_in_binary_tree_2 \
    import Solution, TreeNode


class TestCousinsInBinaryTree(unittest.TestCase):
    def test_cousins_in_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, None, TreeNode(4)),
            TreeNode(3, None, TreeNode(5))
        )
        root2 = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3)
        )
        root3 = TreeNode(1)

        self.assertTrue(solution.isCousins(root1, 5, 4))
        self.assertFalse(solution.isCousins(root2, 4, 3))
        self.assertFalse(solution.isCousins(root3, 2, 3))
