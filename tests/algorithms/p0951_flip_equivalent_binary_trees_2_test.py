import unittest
from leetcode.algorithms.p0951_flip_equivalent_binary_trees_2 \
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
        root3 = TreeNode(
            0,
            TreeNode(4),
            TreeNode(
                1,
                None,
                TreeNode(
                    2,
                    TreeNode(3, TreeNode(5, None, TreeNode(8)), TreeNode(7)),
                    TreeNode(6)
                )
            )
        )
        root4 = TreeNode(
            0,
            TreeNode(
                1,
                None,
                TreeNode(
                    2,
                    TreeNode(6, TreeNode(8)),
                    TreeNode(3, TreeNode(5), TreeNode(7))
                )
            ),
            TreeNode(4)
        )

        self.assertFalse(solution.flipEquiv(TreeNode(1), TreeNode(2)))
        self.assertTrue(solution.flipEquiv(None, None))
        self.assertTrue(solution.flipEquiv(root1, root2))
        self.assertFalse(solution.flipEquiv(root3, root4))
