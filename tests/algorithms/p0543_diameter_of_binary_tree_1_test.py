import unittest
from leetcode.algorithms.p0543_diameter_of_binary_tree_1 \
    import Solution, TreeNode


class TestDiameterOfBinaryTree(unittest.TestCase):
    def test_diameter_of_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3)
        )

        self.assertEqual(3, solution.diameterOfBinaryTree(root))
