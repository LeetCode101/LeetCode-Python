import unittest
from leetcode.algorithms.p0236_lowest_common_ancestor_of_a_binary_tree \
    import Solution, TreeNode


class TestLowestCommonAncestorOfABinaryTree(unittest.TestCase):
    def test_lowest_common_ancestor_of_a_binary_tree(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(5)
        c = TreeNode(1)
        a.left = b
        a.right = c
        c.left = TreeNode(0)
        c.right = TreeNode(8)
        b.left = TreeNode(6)
        e = TreeNode(2)
        e.left = TreeNode(7)
        e.right = TreeNode(4)
        b.right = e

        self.assertEqual(
            3, solution.lowestCommonAncestor(a, TreeNode(5), TreeNode(1)).val)
        self.assertEqual(
            2, solution.lowestCommonAncestor(a, TreeNode(7), TreeNode(4)).val)
        self.assertEqual(
            1, solution.lowestCommonAncestor(a, TreeNode(0), TreeNode(8)).val)
