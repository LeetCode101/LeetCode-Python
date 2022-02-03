import unittest
from leetcode.algorithms.p0662_maximum_width_of_binary_tree \
    import Solution, TreeNode


class TestMaximumWidthOfBinaryTree(unittest.TestCase):
    def test_maximum_width_of_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(3, TreeNode(5), TreeNode(3)),
            TreeNode(2, None, TreeNode(9))
        )

        self.assertEqual(0, solution.widthOfBinaryTree(None))
        self.assertEqual(4, solution.widthOfBinaryTree(root))
