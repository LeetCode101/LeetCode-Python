import unittest
from leetcode.algorithms.p0100_same_tree_1 import Solution, TreeNode


class TestSameTree(unittest.TestCase):
    def test_same_tree(self):
        solution = Solution()
        a = TreeNode(1, TreeNode(2), TreeNode(3))
        b = TreeNode(1, TreeNode(2), TreeNode(3))
        c = TreeNode(1, TreeNode(2))
        d = TreeNode(1, None, TreeNode(2))

        self.assertTrue(solution.isSameTree(a, b))
        self.assertFalse(solution.isSameTree(c, d))
