import unittest
from leetcode.algorithms.p0235_lowest_common_ancestor_of_a_binary_search_tree \
    import Solution, TreeNode


class TestLowestCommonAncestorOfABinarySearchTree(unittest.TestCase):
    def test_lowest_common_ancestor_of_a_binary_search_tree(self):
        solution = Solution()
        a = TreeNode(6)
        b = TreeNode(2)
        c = TreeNode(8)
        a.left = b
        a.right = c
        c.left = TreeNode(7)
        c.right = TreeNode(9)
        b.left = TreeNode(0)
        e = TreeNode(4)
        e.left = TreeNode(3)
        e.right = TreeNode(5)
        b.right = e

        self.assertEqual(
            6, solution.lowestCommonAncestor(a, TreeNode(2), TreeNode(8)).val)
        self.assertEqual(
            8, solution.lowestCommonAncestor(a, TreeNode(7), TreeNode(9)).val)
        self.assertEqual(
            4, solution.lowestCommonAncestor(a, TreeNode(3), TreeNode(5)).val)
