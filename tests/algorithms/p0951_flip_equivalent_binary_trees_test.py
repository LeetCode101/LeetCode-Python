import unittest
from leetcode.algorithms.p0951_flip_equivalent_binary_trees \
    import Solution, TreeNode


class TestFlipEquivalentBinaryTrees(unittest.TestCase):
    def test_flip_equivalent_binary_trees(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4),
                TreeNode(5, TreeNode(7), TreeNode(8))
            ),
            TreeNode(3, TreeNode(6))
        )
        root2 = TreeNode(
            1,
            TreeNode(3, None, TreeNode(6)),
            TreeNode(
                2,
                TreeNode(4),
                TreeNode(5, TreeNode(8), TreeNode(7))
            )
        )

        self.assertTrue(solution.flipEquiv(root1, root2))
