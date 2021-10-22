import unittest
from leetcode.algorithms.p0545_boundary_of_binary_tree \
    import Solution, TreeNode


class TestBoundaryOfBinaryTree(unittest.TestCase):
    def test_boundary_of_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4),
                TreeNode(5, TreeNode(7), TreeNode(8))
            ),
            TreeNode(
                3,
                TreeNode(6, TreeNode(9), TreeNode(10))
            )
        )
        root2 = TreeNode(
            1,
            None,
            TreeNode(2)
        )
        root3 = TreeNode(
            1,
            TreeNode(2)
        )
        root4 = TreeNode(1)
        root5 = TreeNode(
            1,
            TreeNode(2, None, TreeNode(3))
        )

        self.assertListEqual([1, 2, 4, 7, 8, 9, 10, 6, 3],
                             solution.boundaryOfBinaryTree(root1))
        self.assertListEqual([1, 2], solution.boundaryOfBinaryTree(root2))
        self.assertListEqual([1, 2], solution.boundaryOfBinaryTree(root3))
        self.assertListEqual([1], solution.boundaryOfBinaryTree(root4))
        self.assertListEqual([1, 2, 3], solution.boundaryOfBinaryTree(root5))
