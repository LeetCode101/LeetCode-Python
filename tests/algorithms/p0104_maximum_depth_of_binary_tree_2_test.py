import unittest
from leetcode.algorithms.p0104_maximum_depth_of_binary_tree_2 \
    import Solution, TreeNode


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_maximum_depth_of_binary_tree(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(9)
        c = TreeNode(20)
        a.left = b
        a.right = c
        c.left = TreeNode(15)
        c.right = TreeNode(7)

        self.assertEqual(3, solution.maxDepth(a))
