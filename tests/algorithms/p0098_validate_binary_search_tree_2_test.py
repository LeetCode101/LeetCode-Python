import unittest
from leetcode.algorithms.p0098_validate_binary_search_tree_2 \
    import Solution, TreeNode


class TestValidateBinarySearchTree(unittest.TestCase):
    def test_validate_binary_search_tree(self):
        solution = Solution()
        a = TreeNode(2)
        a.left = TreeNode(1)
        a.right = TreeNode(3)

        self.assertTrue(solution.isValidBST(None))
        self.assertTrue(solution.isValidBST(a))

        a = TreeNode(5)
        b = TreeNode(1)
        c = TreeNode(4)
        c.left = TreeNode(3)
        c.right = TreeNode(6)
        a.left = b
        a.right = c

        self.assertFalse(solution.isValidBST(a))
