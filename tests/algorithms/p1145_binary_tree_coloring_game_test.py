import unittest
from leetcode.algorithms.p1145_binary_tree_coloring_game \
    import Solution, TreeNode


class TestBinaryTreeColoringGame(unittest.TestCase):
    def test_binary_tree_coloring_game(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3)
        )
        root2 = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4, TreeNode(8), TreeNode(9)),
                TreeNode(5, TreeNode(10), TreeNode(11))
            ),
            TreeNode(
                3,
                TreeNode(6),
                TreeNode(7)
            )
        )

        self.assertFalse(solution.btreeGameWinningMove(root1, 5, 2))
        self.assertTrue(solution.btreeGameWinningMove(root2, 11, 3))
