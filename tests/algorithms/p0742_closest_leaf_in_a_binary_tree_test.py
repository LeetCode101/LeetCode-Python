import unittest
from leetcode.algorithms.p0742_closest_leaf_in_a_binary_tree \
    import Solution, TreeNode


class TestClosestLeafInABinaryTree(unittest.TestCase):
    def test_closest_leaf_in_a_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(6)))),
            TreeNode(3)
        )

        self.assertEqual(3, solution.findClosestLeaf(root, 2))
