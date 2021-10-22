import unittest
from leetcode.algorithms.p0199_binary_tree_right_side_view_1 \
    import Solution, TreeNode


class TestBinaryTreeRightSideView(unittest.TestCase):
    def test_binary_tree_right_side_view(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(2, None, TreeNode(5)),
            TreeNode(3, None, TreeNode(4))
        )

        self.assertListEqual([], solution.rightSideView(None))
        self.assertListEqual([1, 3, 4], solution.rightSideView(root1))
