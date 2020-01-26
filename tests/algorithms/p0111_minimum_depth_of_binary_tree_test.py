import unittest
from leetcode.algorithms.p0111_minimum_depth_of_binary_tree \
    import Solution, TreeNode


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_minimum_depth_of_binary_tree(self):
        solution = Solution()
        a = TreeNode(3)
        b = TreeNode(9)
        c = TreeNode(20)
        a.left = b
        a.right = c
        c.left = TreeNode(15)
        c.right = TreeNode(7)

        self.assertEqual(2, solution.minDepth(a))
        self.assertEqual(0, solution.minDepth(None))
