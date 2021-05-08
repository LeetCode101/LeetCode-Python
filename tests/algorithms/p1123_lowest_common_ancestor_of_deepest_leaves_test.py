import unittest
from leetcode.algorithms.p1123_lowest_common_ancestor_of_deepest_leaves \
    import Solution, TreeNode


class TestLowestCommonAncestorOfDeepestLeaves(unittest.TestCase):
    def test_lowest_common_ancestor_of_deepest_leaves(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(5)
        c = TreeNode(1)
        a.left = b
        a.right = c
        d = TreeNode(6)
        e = TreeNode(2)
        b.left = d
        b.right = e
        f = TreeNode(0)
        g = TreeNode(8)
        c.left = f
        c.right = g
        h = TreeNode(7)
        i = TreeNode(4)
        e.left = h
        e.right = i

        self.assertEqual(2, solution.lcaDeepestLeaves(a).val)
