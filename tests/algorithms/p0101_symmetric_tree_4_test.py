import unittest
from leetcode.algorithms.p0101_symmetric_tree_4 import Solution, TreeNode


class TestSymmetricTree(unittest.TestCase):
    def test_symmetric_tree(self):
        solution = Solution()
        a = TreeNode(1)
        b = TreeNode(2, TreeNode(3), TreeNode(4))
        c = TreeNode(2, TreeNode(4), TreeNode(3))
        a.left = b
        a.right = c

        self.assertTrue(solution.isSymmetric(None))
        self.assertTrue(solution.isSymmetric(a))
        self.assertFalse(solution.isSymmetric(
            TreeNode(1, TreeNode(2), TreeNode(3))))
        self.assertFalse(solution.isSymmetric(
            TreeNode(1, TreeNode(2, TreeNode(3)))))
