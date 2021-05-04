import unittest
from leetcode.algorithms.p0250_count_univalue_subtrees \
    import Solution, TreeNode


class TestCountUnivalueSubtrees(unittest.TestCase):
    def test_count_univalue_subtrees(self):
        solution = Solution()
        a = TreeNode(5)
        b = TreeNode(1)
        c = TreeNode(5)
        a.left = b
        a.right = c
        b.left = TreeNode(5)
        b.right = TreeNode(5)
        c.right = TreeNode(5)

        self.assertEqual(0, solution.countUnivalSubtrees(None))
        self.assertEqual(4, solution.countUnivalSubtrees(a))
